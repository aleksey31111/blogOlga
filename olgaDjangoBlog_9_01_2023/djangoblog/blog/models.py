import logging
from abc import abstractmethod

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from mdeditor.fields import MDTextField
from uuslug import slugify

from djangoblog.utils import cache_decorator, cache
from djangoblog.utils import get_current_site

logger = logging.getLogger(__name__)


class LinkShowType(models.TextChoices):
    I = ('i', 'титульная страница')
    L = ('l', 'Список')
    P = ('p', 'страница статьи')
    A = ('a', 'Полный сайт')
    S = ('s', 'Страница дружбы со ссылками')


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_time = models.DateTimeField('время создания', default=now)
    last_mod_time = models.DateTimeField('Изменить время', default=now)

    def save(self, *args, **kwargs):
        is_update_views = isinstance(
            self,
            Article) and 'update_fields' in kwargs and kwargs['update_fields'] == ['views']
        if is_update_views:
            Article.objects.filter(pk=self.pk).update(views=self.views)
        else:
            if 'slug' in self.__dict__:
                slug = getattr(
                    self, 'title') if 'title' in self.__dict__ else getattr(
                    self, 'name')
                setattr(self, 'slug', slugify(slug))
            super().save(*args, **kwargs)

    def get_full_url(self):
        site = get_current_site().domain
        url = "https://{site}{path}".format(site=site,
                                            path=self.get_absolute_url())
        return url

    class Meta:
        abstract = True

    @abstractmethod
    def get_absolute_url(self):
        pass


class Article(BaseModel):
    """статья"""
    STATUS_CHOICES = (
        ('d', 'проект'),
        ('p', 'опубликовано'),
    )
    COMMENT_STATUS = (
        ('o', 'Открыть'),
        ('c', 'закрытие'),
    )
    TYPE = (
        ('a', 'статья'),
        ('p', 'страница'),
    )
    title = models.CharField('страница', max_length=200, unique=True)
    body = MDTextField('текст')
    pub_time = models.DateTimeField(
        'время выпуска', blank=False, null=False, default=now)
    status = models.CharField(
        'статус статьи',
        max_length=1,
        choices=STATUS_CHOICES,
        default='p')
    comment_status = models.CharField(
        'статус комментария',
        max_length=1,
        choices=COMMENT_STATUS,
        default='o')
    type = models.CharField('Виды', max_length=1, choices=TYPE, default='a')
    views = models.PositiveIntegerField('Просмотры', default=0)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='автор',
        blank=False,
        null=False,
        on_delete=models.CASCADE)
    article_order = models.IntegerField(
        'Сортировка, чем больше число, тем выше фронт',
        blank=False, null=False, default=0)
    show_toc = models.BooleanField("Отображать ли каталог toc", blank=False, null=False, default=False)
    category = models.ForeignKey(
        'Category',
        verbose_name='Классификация',
        on_delete=models.CASCADE,
        blank=False,
        null=False)
    tags = models.ManyToManyField('Tag', verbose_name='коллекция этикеток', blank=True)

    def body_to_string(self):
        return self.body

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-article_order', '-pub_time']
        verbose_name = "коллекция этикеток"
        verbose_name_plural = verbose_name
        get_latest_by = 'id'

    def get_absolute_url(self):
        return reverse('blog:detailbyid', kwargs={
            'article_id': self.id,
            'year': self.created_time.year,
            'month': self.created_time.month,
            'day': self.created_time.day
        })

    @cache_decorator(60 * 60 * 10)
    def get_category_tree(self):
        tree = self.category.get_category_tree()
        names = list(map(lambda c: (c.name, c.get_absolute_url()), tree))

        return names

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def viewed(self):
        self.views += 1
        self.save(update_fields=['views'])

    def comment_list(self):
        cache_key = 'article_comments_{id}'.format(id=self.id)
        value = cache.get(cache_key)
        if value:
            logger.info('get article comments:{id}'.format(id=self.id))
            return value
        else:
            comments = self.comment_set.filter(is_enable=True).order_by('-id')
            cache.set(cache_key, comments, 60 * 100)
            logger.info('set article comments:{id}'.format(id=self.id))
            return comments

    def get_admin_url(self):
        info = (self._meta.app_label, self._meta.model_name)
        return reverse('admin:%s_%s_change' % info, args=(self.pk,))

    @cache_decorator(expiration=60 * 100)
    def next_article(self):
        # Следующий
        return Article.objects.filter(
            id__gt=self.id, status='p').order_by('id').first()

    @cache_decorator(expiration=60 * 100)
    def prev_article(self):
        # Предыдущая статья
        return Article.objects.filter(id__lt=self.id, status='p').first()


class Category(BaseModel):
    """Классификация статей"""
    name = models.CharField('Имя категории', max_length=30, unique=True)
    parent_category = models.ForeignKey(
        'self',
        verbose_name="родительская категория",
        blank=True,
        null=True,
        on_delete=models.CASCADE)
    slug = models.SlugField(default='no-slug', max_length=60, blank=True)
    index = models.IntegerField(default=0, verbose_name="Сортировка по весу - чем больше, тем выше фронт")

    class Meta:
        ordering = ['-index']
        verbose_name = "Классификация"
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse(
            'blog:category_detail', kwargs={
                'category_name': self.slug})

    def __str__(self):
        return self.name

    @cache_decorator(60 * 60 * 10)
    def get_category_tree(self):
        """
        Рекурсивно получить родительский каталог категории
        :return:
        """
        categorys = []

        def parse(category):
            categorys.append(category)
            if category.parent_category:
                parse(category.parent_category)

        parse(self)
        return categorys

    @cache_decorator(60 * 60 * 10)
    def get_sub_categorys(self):
        """
        Получить все подмножества текущей категории
        :return:
        """
        categorys = []
        all_categorys = Category.objects.all()

        def parse(category):
            if category not in categorys:
                categorys.append(category)
            childs = all_categorys.filter(parent_category=category)
            for child in childs:
                if category not in categorys:
                    categorys.append(child)
                parse(child)

        parse(self)
        return categorys


class Tag(BaseModel):
    """тег статьи"""
    name = models.CharField('название тэга', max_length=30, unique=True)
    slug = models.SlugField(default='no-slug', max_length=60, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:tag_detail', kwargs={'tag_name': self.slug})

    @cache_decorator(60 * 60 * 10)
    def get_article_count(self):
        return Article.objects.filter(tags__name=self.name).distinct().count()

    class Meta:
        ordering = ['name']
        verbose_name = "Этикетка"
        verbose_name_plural = verbose_name


class Links(models.Model):
    """Ссылки"""

    name = models.CharField('имя ссылки', max_length=30, unique=True)
    link = models.URLField('адрес ссылки')
    sequence = models.IntegerField('Сортировать', unique=True)
    is_enable = models.BooleanField(
        'отображать ли', default=True, blank=False, null=False)
    show_type = models.CharField(
        'тип дисплея',
        max_length=1,
        choices=LinkShowType.choices,
        default=LinkShowType.I)
    created_time = models.DateTimeField('время создания', default=now)
    last_mod_time = models.DateTimeField('Изменить время', default=now)

    class Meta:
        ordering = ['sequence']
        verbose_name = 'Ссылки'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class SideBar(models.Model):
    """Боковая панель,
    вы можете отображать некоторый
    HTML-контент"""
    name = models.CharField('заглавие', max_length=100)
    content = models.TextField("содержание")
    sequence = models.IntegerField('Сортировать', unique=True)
    is_enable = models.BooleanField('Включить ли', default=True)
    created_time = models.DateTimeField('время создания', default=now)
    last_mod_time = models.DateTimeField('Изменить время', default=now)

    class Meta:
        ordering = ['sequence']
        verbose_name = 'Боковая панель'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class BlogSettings(models.Model):
    """конфигурация блога"""
    sitename = models.CharField(
        "название веб-сайта",
        max_length=200,
        null=False,
        blank=False,
        default='')
    site_description = models.TextField(
        "Описание Вебсайта",
        max_length=1000,
        null=False,
        blank=False,
        default='')
    site_seo_description = models.TextField(
        "SEO-описание сайта", max_length=1000, null=False, blank=False, default='')
    site_keywords = models.TextField(
        "ключевые слова веб-сайта",
        max_length=1000,
        null=False,
        blank=False,
        default='')
    article_sub_length = models.IntegerField("Длина реферата статьи", default=300)
    sidebar_article_count = models.IntegerField("Количество статей на боковой панели", default=10)
    sidebar_comment_count = models.IntegerField("Количество комментариев на боковой панели", default=5)
    article_comment_count = models.IntegerField("Количество комментариев к статье", default=5)
    show_google_adsense = models.BooleanField('Отображать ли рекламу Google', default=False)
    google_adsense_codes = models.TextField(
        'рекламный контент', max_length=2000, null=True, blank=True, default='')
    open_site_comment = models.BooleanField('Открывать ли функцию комментариев на сайте', default=True)
    beiancode = models.CharField(
        'номер дела',
        max_length=2000,
        null=True,
        blank=True,
        default='')
    analyticscode = models.TextField(
        "код статистики сайта",
        max_length=1000,
        null=False,
        blank=False,
        default='')
    show_gongan_code = models.BooleanField(
        'Отображать ли номер записи общественной безопасности', default=False, null=False)
    gongan_beiancode = models.TextField(
        'Номер записи общественной безопасности',
        max_length=2000,
        null=True,
        blank=True,
        default='')
    resource_path = models.CharField(
        "Адрес для сохранения статического файла",
        max_length=300,
        null=False,
        default='/var/www/resource/')

    class Meta:
        verbose_name = 'конфигурация веб-сайта'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.sitename

    def clean(self):
        if BlogSettings.objects.exclude(id=self.id).count():
            raise ValidationError(_('Может быть только одна конфигурация'))

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        from djangoblog.utils import cache
        cache.clear()

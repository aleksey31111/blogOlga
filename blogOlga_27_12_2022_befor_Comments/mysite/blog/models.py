from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Не опубликован'),
        ('published', 'Опубликован'),
    )
    title = models.CharField(max_length=250, verbose_name='Название поделки')
    slug = models.SlugField(max_length=250, unique_for_date='publish', verbose_name='URL')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d", blank=True, verbose_name="Фото")
    body = models.TextField(verbose_name='Описание поделки')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', verbose_name='Автор')
    publish = models.DateTimeField(default=timezone.now, verbose_name="Время публикации")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время занесения на сайт')
    updated = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='published', verbose_name='Статус публикации')
    # status = models.BooleanField(default=False, verbose_name='Статья опубликована')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категория")

    def __str__(self):
        return self.title

    def get_absolut_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Блог Творчества'
        verbose_name_plural = "Блог Творчеств"
        ordering = ('-created',)


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolut_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

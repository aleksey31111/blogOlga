from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .forms import CommentForm
from .models import Post, Comment

#  Variant 3 - Comment
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ObjectDoesNotExist
from django.template.context_processors import csrf

menu = [
    {'title': 'Добавить поделку', 'url_name': 'index'},
    {'title': 'Войти', 'url_name': 'index'},
]


class BlogHome(ListView):
    model = Post
    template_name = "blog/blogs.html"
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['menu'] = menu
        return context

    def get_queryset(self):
        return Post.objects.filter(status='published').select_related('cat')

    # class Crafts(ListView):
    #     model = Post
    #     template_name = "blog/craft.html"
    #     context_object_name = 'posts'
    #
    #     def get_context_data(self, *, object_list=None, **kwargs):
    #         context = super().get_context_data(**kwargs)
    #         context['title'] = 'Главная страница'
    #         context['cat_selected'] = 0
    #         context['menu'] = menu
    #         return context
    #
    #     def get_queryset(self):
    #         return Post.objects.filter(status='published').select_related('cat')


# Variant 1 - Comment
# class ShowPost(DetailView):
#     model = Post
#     template_name = 'blog/single-blog.html'  # blog/post.html'
#     slug_url_kwarg = 'post_slug'
#     context_object_name = 'post'
#
#     # post = get_object_or_404(Post, slug=slug_url_kwarg)
#     # comments = post.comments.filter(actve=True)
#     # new_comment = None
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = context['post']
#         context['menu'] = menu
#         return context

# Variant 2 - Comment
# class ShowPost(DetailView):
#     model = Post
#     template_name = 'blog/single-blog.html'  # blog/post.html'
#     form_class = CommentForm
#     slug_url_kwarg = 'post_slug'
#     context_object_name = 'post'
#     success_msg = 'Комментарий успешно создан, ожидайте модерации'
#
#     def get_success_url(self):
#         return reverse_lazy('post_slug', kwargs={'pk': self.get_object().id})
#
#     def post(self, request, *args, **kwargs):
#         form = CommentForm
#         if form.is_valid():
#             return self.form_valid(form)
#         else:
#             return self.form_invalid()
#
#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.post = self.get_object()
#         self.object.author = self.request.user
#         self.object.save()
#         return super().form_valid(form)
#
#     def form_invalid(self):
#         return ('Форма заполненна Не Правильно!!!')


# # Comment posted
# if requests == 'POST':
#         comment_form = CommentForm(data=requests)
#         if comment_form.is_valid():
#             # Create Comment object but don't save to database yet
#             new_comment = comment_form.save(commit=False)
#             # Assign the current post to the comment
#             new_comment.post = post
#             # Save the comment to the database
#             new_comment.save()
#     else:
#         comment_form = CommentForm()
#
# def get_context_data(self, *, object_list=None, **kwargs):
#     context = super().get_context_data(**kwargs)
#     context['title'] = context['post']
#     context['menu'] = menu
#     return context


# Variant 3 - Comment
class ShowPost(DetailView, View):
    model = Post
    template_name = 'blog/single-blog.html'  # blog/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'
    comment_form = CommentForm

    # post = get_object_or_404(Post, slug=slug_url_kwarg)
    # comments = post.comments.filter(actve=True)
    # new_comment = None

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['menu'] = menu
        return context

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Post, slug=self.kwargs['article_id'])
        context = {}
        context.update(csrf(request))
        user = auth.get_user(request)
        # Помещаем в контекст все комментарии, которые относятся к статье
        # попутно сортируя их по пути, ID(slug) автоинкрементируемые,
        # поэтому с иерархией не должно возникать.
        context['comments'] = article.comment_set.all().order_by('path')
        context['next'] = article.get_absolut_url()
        # Добавляем форму в случае авторизации пользователя
        if user.is_authenticated:
            context['form'] = self.comment_form

        return render(request, template_name=self.template_name, context=context)


# Декораторы по которым, толко авторизированный пользователб
# может отправить комментарий и только с помощью POST запроса
@login_required()
@require_http_methods(['POST'])
def add_comment(request, article_id):
    form = CommentForm(request.POST)
    article = get_object_or_404(Post, slug=post_slug)
    if form.is_valid():
        comment = Comment()
        comment.path = []
        comment.post_slug = article
        comment.author_id = auth.get_user(request)
        comment.content = form.cleaned_data['CommentForm']
        comment.save()

        # Django Не Позволяет увидеть ID(slug) комментария пока мы не сохраним его,
        # поэтому сформируем path после первого сщхранения
        # и Пересохраним Комментарий.
        try:
            comment.path.extend(Comment.objects.get(slug=form.cleaned_data['comment']))
            comment.path.append(comment.post_slug)
        except ObjectDoesNotExist:
            comment.path.append(comment.post_slug)

        comment.save()
    return redirect(article.get_absolut_url())


# Show category(cat) of Post
class BlogCategory(ListView):
    model = Post
    template_name = 'blog/category.html'  # 'blogs.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(cat__slug=self.kwargs['cat_slug'], status='published').select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория  - ' + str(context['posts'][0].cat)
        context['cat_selected'] = context['posts'][0].cat_id
        context['menu'] = menu
        return context

# Show category(cat) for index
# class BlogCategoryIndex(ListView):
#     model = Post
#     template_name = 'blog/blogs.html'  # 'blogs.html'
#     context_object_name = 'posts'
#     allow_empty = False
#
#     def get_queryset(self):
#         return Post.objects.filter(cat__slug=self.kwargs['cat_slug'], status='published').select_related('cat')
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Категория  - ' + str(context['posts'][0].cat)
#         context['cat_selected'] = context['posts'][0].cat_id
#         context['menu'] = menu
#         return context


# Show category(cat) for single-blog
# class BlogCategorySingleBlog(ListView):
#     model = Post
#     template_name = 'blog/single-blog.html'  # 'blogs.html'
#     context_object_name = 'posts'
#     allow_empty = False
#
#     def get_queryset(self):
#         return Post.objects.filter(cat__slug=self.kwargs['cat_slug'], status='published').select_related('cat')
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Категория  - ' + str(context['posts'][0].cat)
#         context['cat_selected'] = context['posts'][0].cat_id
#         context['menu'] = menu
#         return context

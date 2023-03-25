from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from .forms import CommentForm
from .models import Post
from django.shortcuts import render, get_object_or_404

menu = [
    {'title': 'Добавить поделку', 'url_name': 'index'},
    {'title': 'Войти', 'url_name': 'index'},
]


# Variant 1 From 1
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


# # Variant 1 From 2
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


# Variant 2 From 2
# class ShowPost(DetailView, ):
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


# Variant 1 From 3


def post_detail(request, slug):
    template_name = 'blog/post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    context_object_name = 'posts'
    comments = post.comments.filter(active=True)
    new_comment = None
    # Комментаоий статьи
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Создание Обькта Комментария, Но Не Сохраняя Базу Данных.
            new_comment = comment_form.save(commit=False)
            # Назначить Текущую статьи для Комментария
            new_comment.post = post
            # Сохранить Комментарий в Базе Данных
            new_comment.save()
        else:
            comment_form = CommentForm()

        return render(request, template_name, {'post': post,
                                               'context_object_name': context_object_name,
                                               'new_comment': new_comment,
                                               'comment_form': comment_form})


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

# Variant 2 From 3
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


# Variant 3 From 3
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

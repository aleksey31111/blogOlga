from django.shortcuts import render, redirect
from .models import Articles
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from forms import ArticleForm, AuthUserForm, RegisterUserForm, CommentForm
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect


class HomeListView(ListView):
    model = Articles
    template_name = "blogs.html"
    context_object_name = 'list_articles'


# class LoginRequiredMixin(AccessMixin):
#     def dispatch(self, request, *args, **kwargs):
#         if not request.user.is_authenticated:
#             return self.handle_no_permission()
#         return super().dispatch(request, *args, **kwargs)


# class HomeDetailView(DetailView):
#     model = Articles
#     template_name = 'detail.html'
#     context_object_name = 'get_article'
#     success_msg = 'Комментарий успешно создан, ожидайте модерации'
#
#     def get_success_url(self):
#         return reverse_lazy('detail_page', kwargs={'pk': self.get_object().id})
#
#     def post(self, request, *args, **kwargs):
#         form = self.get_form()
#         if form.is_valid():
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)
#
#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.article = self.get_object()
#         self.object.author = self.request.user
#         self.object.save()
#         return super().form_valid(form)


class HomeDetailView(FormMixin, DetailView):
    model = Articles
    template_name = 'detail.html'
    context_object_name = 'get_article'
    form_class = CommentForm


class CustomSuccessMessageMixin:
    @property
    def success_msq(self):
        return False

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super().form_valid(form)

    def get_success_url(self):
        return '%s?id=%s' % (self.success_url, self.object.id)


    class ArticleCreateView(LoginRequiredMixin, CustomSuccessMessageMixin, CreateView):
        login_url = reverse_lazy('login_page')
        model = Articles
        template_name = 'edit_page.html'
        form_class = ArticleForm
        success_url = reverse_lazy('edit_page')
        success_msg = 'Запись сщздана'
        def get_context_data(self, **kwargs):
            kwargs['list_articles'] = Articles.object.all().order_by('-id')
            return super().get_context_data(**kwargs)
        def form_valid(self,form):
            self.object = form.save(commit=False)


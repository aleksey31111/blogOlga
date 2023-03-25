from django.urls import path, re_path
# from django.contrib.auth import views as auth_views
from .views import BlogHome, ShowPost, BlogCategory, add_comment, Comment  # Crafts,

app_name = 'post'

urlpatterns = [

    # path('craft/', Crafts.as_view(), name="craft"),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    # re_path(r'^(?P<article\_id>[0-9]+)/$', views.EArticleView.as\_view(), name='article'),
    # re_path(r'^comment/(?P<article_id>[0-9]+)/$', views.add_comment, name='add_comment'),
    path('^comment/<slug:post_slug>', add_comment, name='add_comment'),
    path('category/<slug:cat_slug>/', BlogCategory.as_view(), name="category"),
    path('', BlogHome.as_view(), name="index"),
]

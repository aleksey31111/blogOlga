from django.urls import path
# from django.contrib.auth import views as auth_views
from .views import BlogHome, BlogCategory, post_detail  # Crafts, ShowPost,

urlpatterns = [

    # path('crafts/', Crafts.as_view(), name="crafts"),
    # path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', BlogCategory.as_view(), name="category"),
    path('', BlogHome.as_view(), name="index"),
    # path('<slug:slug>/', post_detail, name='post_detail'),
    path('<slug:post_slug>/', post_detail, name='post_detail'),

]

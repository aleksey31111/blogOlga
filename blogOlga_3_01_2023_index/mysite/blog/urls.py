from django.urls import path
# from django.contrib.auth import views as auth_views
from .views import BlogHome, ShowPost, BlogCategory  # Crafts,

urlpatterns = [

    # path('crafts/', Crafts.as_view(), name="crafts"),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', BlogCategory.as_view(), name="category"),
    path('', BlogHome.as_view(), name="index"),
]

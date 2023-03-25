from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # path("blog/", views.blog, name='blog'),
    # path('', views.index, name='crafts_index'),
    path('', views.crafts(), name='crafts_index'),
    # path('<int:blog_id>/', views.detail, name="detail"),
    path('<int:crafts_id>/', views.detail, name="detail"),
]

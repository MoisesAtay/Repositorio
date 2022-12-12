from django.urls import path
from .views import render_posts,post_detail,create_blog,add_blog

app_name = 'blog'

urlpatterns = [
    path('',render_posts,name="posts"),
    path('<int:post_id>', post_detail, name="post_detail"),
    path('create_blog/',create_blog, name="create_blog"),
    path('add_blog',add_blog),
    
]

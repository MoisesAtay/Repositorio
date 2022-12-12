from django.shortcuts import render,get_object_or_404
from .models import Post

# Create your views here.

def render_posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html',{'posts': posts })

def post_detail(request,post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post_detail.html',{'post': post}) 

def create_blog(request):
    return render(request, 'create_blog.html')

def add_blog(request):
    title=request.POST['title']
    description = request.POST['description']
    image = request.FILES['image']
    date = request.POST['date']

    post=Post.objects.create(title=title, description=description, image=image, date=date)

    return render(request,'posts.html')
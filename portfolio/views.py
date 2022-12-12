from django.shortcuts import render,redirect
from .models import Project
# Create your views here.

def home(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'projects': projects})

def form(request):
    return render(request, 'form.html')

def registrar(request):
    title = request.POST['title']
    description = request.POST['description']
    image = request.FILES['image']
    url = request.POST['url']

    project = Project.objects.create(title=title, description=description, image=image, url=url)

    return render(request, 'home.html')


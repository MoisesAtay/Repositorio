from django.urls import path
from .views import home,form,registrar

app_name = 'portfolio'

urlpatterns = [
    path('',home,name="home"),
    path('form/',form, name="form"),
    path('registrar/',registrar),
]

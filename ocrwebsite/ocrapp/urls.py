from django.urls import path
from . import views

urlpatterns = [
    path('homepage',views.index, name = 'index'),
    path('',views.simple_upload, name = 'upload'),
]
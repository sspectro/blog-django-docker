from django.contrib import admin
from django.urls import path
from blog.views import index

app_name = 'blog'

urlpatterns = [
    # blog:index
    path('', index, name='index'),
]



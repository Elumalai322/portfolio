from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('', include('blog.urls')),  # Blog app URLs connect
]

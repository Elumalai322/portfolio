from django.contrib import admin
from django.urls import path
from blog import views  # Import views from the blog app
from blog.views import contact_view  # Import the contact view correctly

urlpatterns = [
    path('', views.about, name='about'),         # Home or about page
    path('contact/', contact_view, name='contact'),  # Contact form endpoint
]


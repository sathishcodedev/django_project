from django.urls import path
from . import views

# The URL patterns for the blog app
url_patterns = [
    path("",views.index, name="index")
]
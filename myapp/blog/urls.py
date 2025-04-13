from django.urls import path
from . import views

# The URL patterns for the blog app
urlpatterns = [
    path("",views.index, name="index")
]
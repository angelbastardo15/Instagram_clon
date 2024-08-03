from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
from publicaciones.models import post

class HomePageView(ListView):

    model= post
    template_name="home.html"
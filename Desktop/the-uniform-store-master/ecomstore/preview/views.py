# Create your views here.

from django.shortcuts import render_to_response

def home(request):
    site_name = "The Uniform Store"
    return render_to_response("home.html", { 'site_name' : site_name })

def info(request):
    site_name = "The Uniform Store"
    return render_to_response("info.html", { 'site_name' : site_name  })


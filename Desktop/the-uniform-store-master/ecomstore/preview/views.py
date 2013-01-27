# Create your views here.

from django.shortcuts import render_to_response

def home(request):
    site_name = "The Uniform Store"
    return render_to_response("home.html", { 'site_name' : site_name })

def info(request):
    site_name = "The Uniform Store"
    return render_to_response("info.html", { 'site_name' : site_name  })

def scopes_for_the_cure(request):
    site_name = "The Uniform Store"
    return render_to_response("scopes/scopes-for-the-cure.html", { 'site_name' : site_name })

def james_cancer_hospital(request):
    site_name = "The Uniform Store"
    return render_to_response("scopes/james-cancer-hospital.html", { 'site_name' : site_name })

def mount_carmel(request):
    site_name = "The Uniform Store"
    return render_to_response("scopes/mount-carmel.html", { 'site_name' : site_name })

def nationwide_childrens(request):
    site_name = "The Uniform Store"
    return render_to_response("scopes/nationwide-childrens.html", { 'site_name' : site_name })

def ohio_health(request):
    site_name = "The Uniform Store"
    return render_to_response("scopes/ohio-health.html", { 'site_name' : site_name }) 



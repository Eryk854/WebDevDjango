from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,"PD1/home_page.html")

def languages(request):
    return render(request, "PD1/programing_languages.html")
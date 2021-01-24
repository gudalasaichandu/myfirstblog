from django.shortcuts import render
from django.conf import settings

# Create your views here.
def index(request):
    context={
        'name':settings.DATA['name'],
        'about_me':settings.DATA['about_me']
    }
    return render(request,'app1/index.html',context)
def about(request):
    return render(request, 'app1/aboutMe.html')

def page3(request):
    return render(request, 'app1/page3.html')

def project(request):
    context={}
    return render(request,'app1/project.html',context)

def languages(request):
    context={}
    return render(request,'app1/languages.html',context)
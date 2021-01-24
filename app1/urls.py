from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('project/',views.project,name='projects'),
    path('languages/',views.languages,name='languages'),
    path('about/',views.about),
    path('page3/',views.page3),
    path('',views.index,name='index')

]

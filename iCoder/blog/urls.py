from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [

    # Api for post Comments
    path('postComment', views.postComment, name='postComment'),

    path('', views.blogHome, name='blogHome'),
    path('<str:slug>', views.blogPost, name='blogPost'),


    #path('postComment', views.postComment, name='postComment'),


]
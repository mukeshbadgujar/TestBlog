from django.shortcuts import render, HttpResponse


# Create your views here.
def blogHome(request):
    return HttpResponse("This is Blog Home")

def blogPost(request, slug):
    return HttpResponse(f'This is Blog Post {slug}')
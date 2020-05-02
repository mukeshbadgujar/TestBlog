from django.shortcuts import render, HttpResponse


# Create your views here.
def blogHome(request):
    return render(request, 'blog/blogHome.html')
    #return HttpResponse("This is Blog Home")

def blogPost(request, slug):
    return render(request, 'blog/blogPost.html')
    #return HttpResponse(f'This is Blog Post {slug}')
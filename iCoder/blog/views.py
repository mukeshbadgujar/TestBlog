from django.shortcuts import render, HttpResponse, redirect
from .models import Post, BlogComment

# Create your views here.
def blogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts':allPosts}
    return render(request, 'blog/blogHome.html', context)
    #return HttpResponse("This is Blog Home")

def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post) # get posts comments
    context = {'post':post, 'comments':comments}
    return render(request, 'blog/blogPost.html', context)
    #return HttpResponse(f'This is Blog Post {slug}')

def postComment(request):
    if request.method == "POST":
       pass
    return redirect('home')
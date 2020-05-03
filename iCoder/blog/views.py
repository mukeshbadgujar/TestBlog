from django.shortcuts import render, HttpResponse, redirect
from .models import Post, BlogComment
from django.contrib import messages


# Create your views here.
def blogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts':allPosts}
    return render(request, 'blog/blogHome.html', context)
    #return HttpResponse("This is Blog Home")

def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post, parent=None) # get posts comments
    replies = BlogComment.objects.filter(post=post).exclude(parent=None) # get posts comments
    replyDict ={}
    for reply in replies:
        if reply.sno not in replyDict.keys():
            replyDict[reply.sno] = [reply]
        else:
            replyDict[reply.sno].append(reply)
    context = {'post':post, 'comments':comments, 'user':request.user, 'replyDict':replyDict}
    return render(request, 'blog/blogPost.html', context)
    #return HttpResponse(f'This is Blog Post {slug}')

def postComment(request):
    if request.method == "POST":
        comment = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get("postSno")
        post = Post.objects.get(sno=postSno)
        parentReplySno = request.POST.get("parentReplySno")

        if parentReplySno == "":
            comment = BlogComment(comment=comment, user=user, post=post)
            comment.save()
            messages.success(request, "Commented Successfully!!!")
        else:
            parent = BlogComment.objects.get(sno=parentReplySno)
            comment = BlogComment(comment=comment, user=user, post=post, parent=parent)

            comment.save()
            messages.success(request, "Replyied Successfully!!!")

    return redirect(f"/blog/{post.slug}")
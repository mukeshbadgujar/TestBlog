from django.shortcuts import render, HttpResponse, redirect
from . models import Contact
from blog.models import Post
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, 'home/home.html')
    #return HttpResponse("This is Home")

def about(request):
    messages.error(request, 'Welcome to Contact!!')
    return render(request, 'home/about.html')
    #return HttpResponse("This is about")

def contact(request):
    #messages.success(request, 'Welcome to Contact!!')
    if request.method =='POST':
        nameContact = request.POST['nameContact']
        emailContact = request.POST['emailContact']
        phoneContact = request.POST['phoneContact']
        descContact = request.POST['descContact']

        if len(nameContact)<2 or len(emailContact)<3 or len(phoneContact)<10 or len(descContact)<3:
            messages.error(request, "Plzz Fill the Form Correctly")
        else:
            contact = Contact(name=nameContact, email=emailContact, phone=phoneContact, content=descContact)
            contact.save()
            messages.success(request, "Your Form is Submitted")
    return render(request, 'home/contact.html')
    #return HttpResponse("This is contact")

def search(request):
    query = request.GET['query']
    if len(query) > 100:
        allPosts = Post.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)

    if allPosts.count() == 0:
        messages.warning(request, "Plzz Correct the Query")
    context = {'allPosts':allPosts, 'query':query}
    return render(request, 'home/search.html', context)

def handleSignup(request):
    if request.method == "POST":
        fnameSignUp = request.POST['fnameSignUp']
        lnameSignUp = request.POST['lnameSignUp']
        usernameSignUp = request.POST['usernameSignUp']
        emailSignUp = request.POST['emailSignUp']
        passSignUp = request.POST['passSignUp']
        confPassSignUp = request.POST['confPassSignUp']

        # Check for errorneous input
        if len(usernameSignUp)>10:
            messages.error(request, "Username Must Be under 10 char")
            return redirect('home')
        # if contain numbers in uname
        if not usernameSignUp.isalnum():
            messages.error(request, "Username must be only character")
            return redirect('home')
        # match password
        if passSignUp != confPassSignUp:
            messages.error(request, "Password Not Match")
            return redirect('home')
        # Create User
        myuser = User.objects.create_user(usernameSignUp, emailSignUp, passSignUp)
        myuser.first_name = fnameSignUp
        myuser.last_name = lnameSignUp
        myuser.save()
        messages.success(request, "Your Account is Succesfully Created")
        return redirect('home');
    else:
        return HttpResponse("404 Not Found")

def handleLogin(request):
    if request.method == "POST":
        usernameLogin = request.POST['usernameLogin']
        passwordLogin = request.POST['passwordLogin']

        user = authenticate(username=usernameLogin, password=passwordLogin)

        if user is not None:
            login(request, user)
            messages.success(request, "Succesfully Login")
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials, Plzz Try Again")
            return redirect('home')

    return HttpResponse("404 Not Found")

def handleLogout(request):
    logout(request)
    messages.success(request, "Succesfully Logged Out")
    return redirect('home')
    #return HttpResponse("404 Not Found")
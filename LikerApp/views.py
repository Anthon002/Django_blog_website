from django.http import HttpResponseRedirect,Http404
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from .forms import *
from django.contrib import messages
from .models import *
from .decorators import *
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.db.models import Q 
#from .filters import SearchFilter

# Create your views here.
@unauthenticated_user
def register(request):
    createUser=CreationUserForm()
    if request.method == 'POST':
        createUser=CreationUserForm(request.POST)
        if createUser.is_valid():
            createUser.save()
    context={
        'createUser':createUser
    }
    return render(request,'pages/registerPage.html',context)

@unauthenticated_user
def loginUser(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('LikerApp:public_post')
        else:
            messages.info(request,'username or password is incorrect ')
    return render(request,'pages/login.html')

def logoutUser(request):
    logout(request)
    return redirect('LikerApp:loginUser')

@login_required(login_url='/login')
def publicPost(request):
    posts=Post.objects.all().order_by('-created_at')
    profile= Profile.objects.all()
    #searchFilter = SearchFilter( request.GET, queryset=posts)
    #posts=searchFilter.qs
    user= request.user
    context={
        'posts':posts,
        'user':user,
        'profile':profile,
        #'searchFilter':searchFilter
    }
    return render(request,'pages/publicPost.html/',context)
@login_required(login_url='/login')
def searchPost(request):
    query=request.GET.get("search")
    if query:
        result=Post.objects.filter( Q(title__icontains=query)| Q(content__icontains=query) | Q(profile__user__username__icontains=query))
    else:
        result=""
    context={
        'result':result
    }
    return render(request,'pages/postSearch.html',context)
@login_required(login_url='/login')
def specificPost(request,pk):
    post=Post.objects.get(id=pk)
    context={
        "post":post
    }
    return render(request,'pages/specificPost.html/',context)

@login_required(login_url='/login')
def personalPost(request,pk):
    personalPosts=Post.objects.filter(profile=Profile.objects.get(id=pk))
    context={
        "personalPosts":personalPosts
    }
    return render(request,"pages/personalPost.html",context)

@login_required(login_url='/login')
def profilePage(request,pk):
    profile=Profile.objects.get(id=pk)
    post=profile.post_set.all()
    context={
        'profiles':profile,
        'posts':post
    }
    return render(request,'pages/profilePage.html',context)

@login_required(login_url='/login')
def createPost(request,pk):
    profile=Profile.objects.get(id=pk)
    user= get_object_or_404(User,id=pk)
    if request.user != user:
        raise Http404("You are not authorized to view this page.")
    orderFormSet=inlineformset_factory(Profile,Post, fields=('title','content'),extra=1)
    formset=orderFormSet(queryset=Post.objects.none(),instance=profile)
    if request.method == 'POST':
        formset=orderFormSet(request.POST,instance=profile)
        if formset.is_valid():
            formset.save()
            return redirect('/post')
    context={
        'formset':formset,
    }
    return render(request,'pages/createPost.html',context)

@login_required(login_url='/login')
def delete(request,pk):
    post=Post.objects.get(id=pk)
    if request.method == "POST":
        post.delete()
        return redirect("/post")
    context={"item":post}
    return render (request,'pages/delete.html',context)

@login_required(login_url='/login')
def like_post(request):
    user=request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)
        
        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)
            
        like, created = Like.objects.get_or_create(user=user, post_id=post_id)
        
        if not created:
            if like.value == 'Like':
                like.value = ' Unlike'
            else:
                like.value = 'Like'
            
            like.save()
        context={
            'post':post_obj
        }
    return redirect( reverse('LikerApp:specificPost',args=[post_obj.id]) )
@login_required(login_url='/login')
def comment_post(request,pk):
    #users=request.user
    posts=Post.objects.get(id=pk)
    commentFormSet=inlineformset_factory(Post,Comment,fields=('content',),extra=1)
    formset=commentFormSet(queryset=Comment.objects.none(),instance=posts)
    if request.method == 'POST':
        formset=commentFormSet(request.POST,instance=posts)
        if formset.is_valid():
            formset.save()
            return redirect("/post")
    context={
        "formset":formset,
    }
    return render(request,'pages/createComment.html',context)

@login_required(login_url='/login')
def display_comments(request,pk):
    posts=Post.objects.get(id=pk)
    pcomment=Comment.objects.filter(post=posts)
    context={
        'pcomment':pcomment
    }
    return render(request,'pages/displayComment.html',context)

#Change profile picture
@login_required(login_url='/login')
def customerSettings(request):
    customerForm= SettingsForm(instance=request.user.profile)
    if request.method == "POST":
        customerForm=SettingsForm(request.POST,request.FILES, instance=request.user.profile)
        if customerForm.is_valid():
            customerForm.save()
            #return redirect('/post')
        else:
            return redirect('/')
    context={
        'form':customerForm
    }
    return render(request,'pages/customer_settings.html',context)

@login_required(login_url='/login')
def changeUsername(request):
    uForm=UsernameForm(instance = request.user)
    if request.method == "POST":
        uForm = UsernameForm(request.POST, instance= request.user)
        uForm.save()
    context={
        'uForm':uForm
    }
    return render(request,'pages/changeUsername.html',context)

@login_required(login_url='/login')
def settingsPage(request):
    return render(request,'pages/settings.html/')
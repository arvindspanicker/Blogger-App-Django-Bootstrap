from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
import json
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import PostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
import datetime

# Create your views here.
def profile(request):
    if request.user.is_authenticated:
        return render(request, 'blog/profile.html') 
    else:
        return HttpResponseRedirect('/login')

def home(request):
    if request.user.is_authenticated:
        posts_list = Post.objects.all().order_by("-timestamp")
        searchquery = request.GET.get("searchquery")
        if searchquery:
            posts_list = posts_list.filter(Q(tags=searchquery)| Q(title=searchquery)| Q(author_name=searchquery)).distinct()
        paginator = Paginator(posts_list,5)
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        context = {
            'posts':posts
        }
        return render(request, 'blog/home.html',context)
    else:
        return HttpResponseRedirect('/login')

def addblog(request):
    if request.user.is_authenticated:
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author_id = request.user.id
            instance.author_name = request.user.username
            instance.save()
            return HttpResponseRedirect('/home/')
        context = {
            'form':form,
        }
        return render(request, 'blog/post_form.html', context)
    else:
        return HttpResponseRedirect('/login')

def blog(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            comment = request.POST['comment-text']
            post_id = id
            comment_author = request.user.username
            com = Comment(comment = comment, post_id = post_id, comment_author = comment_author)
            com.save()
            link = '/home/blog/' + str(int(id))
            return redirect(link)
        else:
            post_id = str(id)
            post = Post.objects.get(id = post_id)
            comments = Comment.objects.filter(post_id = id)
            context = {
                'post':post,
                'comments':comments
            }
            return render(request, 'blog/blog.html', context)
    else:
        return HttpResponseRedirect('/login')

def chat(request,room_name):
    if request.user.is_authenticated:
        chatroomname = request.GET.get("chatroomname")
        time_now = datetime.datetime.now()
        if chatroomname:
            link = '/home/chat/' + chatroomname
            return HttpResponseRedirect(link, {'room_name_json': mark_safe(json.dumps(room_name)),'user_name': mark_safe(json.dumps(request.user.username)), 'chat_room': chatroomname, 'time_now':time_now} ) 
        else:
            return render(request, 'blog/chat.html', {'room_name_json': mark_safe(json.dumps(room_name)),'user_name': mark_safe(json.dumps(request.user.username)), 'chat_room': chatroomname, 'time_now':time_now})
    else:
        return HttpResponseRedirect('/login')


def editblog(request, id):
    if request.user.is_authenticated:
        post_id = int(id)
        print(post_id)
        post = Post.objects.get(id = post_id)
        form = PostForm(request.POST or None, request.FILES or None,instance = post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author_id = request.user.id
            instance.author_name = request.user.username
            instance.save()
            link = '/home/blog/' + str(post_id)
            return HttpResponseRedirect(link)
        context = {
            'post':post,
            'form':form,
        }
        return render(request, 'blog/post_form.html', context)
    else:
        return HttpResponseRedirect('/login')
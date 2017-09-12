# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User

from django.shortcuts import (render, get_object_or_404)
from django.conf import settings
from django.utils import timezone
#from django.CMS.files.storage import FileSystemStorage
from .forms import PostForm
from .models import Post, Link

def link_list(request):
    links = Link.objects.all()
    return render(request, 'CMS/linklist.html', {'links': links})

def calendar(request):
    return render(request, 'CMS/calendar.html')

def post_list(request):
    
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #return render(request, 'CMS/post_list.html', {'posts': posts})

    return render(request, 'CMS/post_list.html', {'posts': posts})

def my_view(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.username
    return render(request, 'CMS/base.html', username)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'CMS/post_detail.html', {'post': post})


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'CMS/post_edit.html', {
        'form': form
    })


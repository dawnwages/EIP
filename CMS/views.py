# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.utils import timezone
#from django.CMS.files.storage import FileSystemStorage
from .forms import UploadFileForm
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'CMS/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'CMS/post_detail.html', {'post': post})


def simple_upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = ModelWithFileField(file_field=request.FILES['myfile'])
            instance.save()
            return redirect('home')
    else:
        form = UploadFileForm()
    return render(request, 'CMS/simple_upload.html', {'form': form})


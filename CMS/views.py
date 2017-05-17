# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.conf import settings
#from django.CMS.files.storage import FileSystemStorage
from .forms import UploadFileForm
from .models import Post

def post_list(request):
	return render(request, 'CMS/post_list.html', {})

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
from django import forms
#from uploads.CMS.models import asset
from .models import Post

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'email', 'url', 'Update_Choices', 'text', 'asset',)
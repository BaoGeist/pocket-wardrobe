from socket import fromshare
from django import forms 
from django.forms import ModelForm
from .models import Wardrobe

class PostForm(ModelForm):

    class Meta:
        model = Wardrobe
        fields = ('clothing',)


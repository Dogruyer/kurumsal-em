from django import forms
from django.forms.models import ModelForm
from .models import *


class BasicForm(ModelForm):
    class Meta:
        model = Mail


class YeniBannerForm(ModelForm):
    class Meta:
        model = Banner

        def save(self, user):
            yeni = Banner()
            yeni.title = self.cleaned_data.get('title')
            yeni.image = self.cleaned_data.get('banner_image')
            yeni.save()
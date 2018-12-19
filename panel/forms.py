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

class YeniSliderForm(ModelForm):
    class Meta:
        model = Slider

        def save (self,user):
            yeni = Slider()
            yeni.image = self.cleaned_data.get('slider_image')
            yeni.save()

class Yenialtkategoriresimtablo(ModelForm):
    class Meta:
        model = Kategori

        def save(self, user):
            yeni = Kategori()
            yeni.title = self.cleaned_data.get('title')
            yeni.image = self.cleaned_data.get('kategori_image')
            yeni.save()

class Yenikoleksiyontablo(ModelForm):
    class Meta:
        model = Koleksiyonlar

        def save(self, kategori_nesne):
            yeni = Koleksiyonlar()
            yeni.title = self.cleaned_data.get('title')
            yeni.content = self.cleaned_data.get('content')
            yeni.image = self.cleaned_data.get('koleksiyon_image')
            yeni.kategori = kategori_nesne
            yeni.save()

class Yenikarttablo(ModelForm):
    class Meta:
        model = Kartlar

        def save(self, user):
            yeni = Kartlar()
            yeni.title = self.cleaned_data.get('title')
            yeni.image = self.cleaned_data.get('kart_image')
            yeni.save()

class Yeniblogtablo(ModelForm):
    class Meta:
        model = Blog

        def save(self, user):
            yeni = Blog()
            yeni.title = self.cleaned_data.get('title')
            yeni.content = self.cleaned_data.get('content')
            yeni.image = self.cleaned_data.get('blog_image')
            yeni.save()

class Yenifootertablo(ModelForm):
    class Meta:
        model = Footer

        def save(self, user):
            yeni = Footer()
            yeni.title = self.cleaned_data.get('slogan')
            yeni.title = self.cleaned_data.get('adres')
            yeni.title = self.cleaned_data.get('telefon')
            yeni.email = self.cleaned_data.get('email')
            yeni.save()

class Yenikategoribannertablo(ModelForm):
    class Meta:
        model = Urun

        def save(self, user):
            yeni = Urun()
            yeni.title = self.cleaned_data.get('title')
            yeni.content = self.cleaned_data.get('content')
            yeni.image = self.cleaned_data.get('urun_image')
            yeni.save()

class Yenirenklertablo(ModelForm):
    class Meta:
        model = Renkler

        def save(self, user):
            yeni = Renkler()
            yeni.title = self.cleaned_data.get('title')
            yeni.image = self.cleaned_data.get('renk_image')
            yeni.save()

class Yenihakkimizdatablo(ModelForm):
    class Meta:
        model = Hakkimizda

        def save(self, user):
            yeni = Hakkimizda()
            yeni.title = self.cleaned_data.get('title')
            yeni.title = self.cleaned_data.get('content')
            yeni.image = self.cleaned_data.get('hakkimizda_gorsel')
            yeni.image = self.cleaned_data.get('sayfa_gorseli')
            yeni.save()


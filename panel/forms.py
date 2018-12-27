from django import forms
from django.forms.models import ModelForm
from .models import *
from .utils import image_resizer

class YeniKategoriForm(ModelForm):
    class Meta:
        model = Kategori

        def save(self, user):
            yeni = Kategori()
            yeni.title = self.cleaned_data.get('title')
            yeni.save()

class YeniKoleksiyonKategoriForm(ModelForm):
    class Meta:
        model = KoleksiyonKategori

        def save(self, user):
            yeni = KoleksiyonKategori()
            yeni.title = self.cleaned_data.get('title')
            yeni.save()


class YeniSliderForm(ModelForm):
    class Meta:
        model = Slider

        def save (self,user):
            yeni = Slider()
            yeni.slider_image = self.cleaned_data.get('slider_image')
            yeni.save()
            image_resizer(yeni.slider_image)


class Yenialtkategoriresimtablo(ModelForm):
    class Meta:
        model = Kategori_bolumu

        def save(self, user):
            yeni = Kategori()
            yeni.title = self.cleaned_data.get('title')
            yeni.kategori_image = self.cleaned_data.get('kategori_image')
            yeni.save()

class Yenikoleksiyontablo(ModelForm):
    class Meta:
        model = Koleksiyonlar
        exclude = ["koleksiyonkategori"]


class Yenikarttablo(ModelForm):
    class Meta:
        model = Kartlar

        def save(self, user):
            yeni = Kartlar()
            yeni.title = self.cleaned_data.get('title')
            yeni.kart_image = self.cleaned_data.get('kart_image')
            yeni.save()

class Yeniblogtablo(ModelForm):
    class Meta:
        model = Blog

        def save(self, user):
            yeni = Blog()
            yeni.title = self.cleaned_data.get('title')
            yeni.content = self.cleaned_data.get('content')
            yeni.blog_image = self.cleaned_data.get('blog_image')
            yeni.save()

class Yenifootertablo(ModelForm):
    class Meta:
        model = Footer

        def save(self, user):
            yeni = Footer()
            yeni.slogan = self.cleaned_data.get('slogan')
            yeni.adres = self.cleaned_data.get('adres')
            yeni.telefon = self.cleaned_data.get('telefon')
            yeni.email = self.cleaned_data.get('email')
            yeni.save()

class Yenikategoribannertablo(ModelForm):
    class Meta:
        model = Urun
        exclude = ["kategori_id"]


class Yenirenklertablo(ModelForm):
    class Meta:
        model = Renkler

        def save(self, user):
            yeni = Renkler()
            yeni.title = self.cleaned_data.get('title')
            yeni.renk_image = self.cleaned_data.get('renk_image')
            yeni.save()

class Yenihakkimizdatablo(ModelForm):
    class Meta:
        model = Hakkimizda

        def save(self, user):
            yeni = Hakkimizda()
            yeni.title = self.cleaned_data.get('title')
            yeni.title = self.cleaned_data.get('content')
            yeni.hakkimizda_gorsel = self.cleaned_data.get('hakkimizda_gorsel')
            yeni.sayfa_gorseli = self.cleaned_data.get('sayfa_gorseli')
            yeni.save()

class YeniDetailfotoForm(ModelForm):
    class Meta:
        model = Detailfoto
        exclude = ["urun_key"]

class YeniDetailfeatureForm(ModelForm):
    class Meta:
        model = Detailfeature

        def save(self, user):
            yeni = Detailfeature()
            yeni.content = self.cleaned_data.get('content')
            yeni.save()


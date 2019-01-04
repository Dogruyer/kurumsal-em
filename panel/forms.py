from django import forms
from django.forms.models import ModelForm
from .models import *


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

class Yenialtkategoriresimtablo(ModelForm):
    class Meta:
        model = Kategori_bolumu

class Yenikoleksiyontablo(ModelForm):
    class Meta:
        model = Koleksiyonlar
        exclude = ["koleksiyonkategori"]

class Yenikarttablo(ModelForm):
    class Meta:
        model = Kartlar

class Yeniblogtablo(ModelForm):
    class Meta:
        model = Blog

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

class Yenihakkimizdatablo(ModelForm):
    class Meta:
        model = Hakkimizda

class YeniDetailfotoForm(ModelForm):
    class Meta:
        model = Detailfoto
        exclude = ["urun_key"]

class YeniDetailfeatureForm(ModelForm):
    class Meta:
        model = Detailfeature

        exclude = ["urun_key"]

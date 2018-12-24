# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render_to_response,render,HttpResponse
from django.core.context_processors import csrf

from django.shortcuts import render
from django.shortcuts import render, HttpResponse, render_to_response, redirect
from django.core.urlresolvers import reverse
from panel.models import *
from django.core.context_processors import csrf

def home(request):
    kategori = Kategori.objects.all()

    slider = Slider.objects.all()

    altresim = Kategori_bolumu.objects.all()
    altresim_uzunluk = len(altresim)
    ilk_banner = altresim[altresim_uzunluk-1]
    ikinci_banner = altresim[altresim_uzunluk-2]
    ucuncu_banner = altresim[altresim_uzunluk-3]
    dorduncu_banner = altresim[altresim_uzunluk-4]
    besinci_banner = altresim[altresim_uzunluk-5]

    koleksiyon_baslik = KoleksiyonKategori.objects.all()


    c = {"kategori": kategori,
         "slider": slider,
         "altresim": altresim,
         "ilk_banner": ilk_banner,
         "ikinci_banner": ikinci_banner,
         "ucuncu_banner": ucuncu_banner,
         "dorduncu_banner": dorduncu_banner,
         "besinci_banner": besinci_banner,
         "koleksiyon_baslik": koleksiyon_baslik}

    return render(request, "home/index.html", c)

def shop(request):
    return render(request, "home/shop.html")

def productdetail(request):
    return render(request, "home/productdetail.html")

def colors(request):
    return render(request, "home/colors.html")

def aboutus(request):
    return render(request, "home/aboutus.html")

def contactus(request):
    return render(request, "home/contactus.html")
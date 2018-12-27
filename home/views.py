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
    footer = Footer.objects.all()
    kategori = Kategori.objects.all()
    slider = Slider.objects.all()
    kart = Kartlar.objects.all()
    blog = Blog.objects.all()
    koleksiyon = Koleksiyonlar.objects.all()


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
         "kart": kart,
         "blog": blog,
         "koleksiyon": koleksiyon,
         "footer": footer,
         "altresim": altresim,
         "ilk_banner": ilk_banner,
         "ikinci_banner": ikinci_banner,
         "ucuncu_banner": ucuncu_banner,
         "dorduncu_banner": dorduncu_banner,
         "besinci_banner": besinci_banner,
         "koleksiyon_baslik": koleksiyon_baslik}

    return render(request, "home/index.html", c)

def shop(request, id):
    footer = Footer.objects.all()
    kategori = Kategori.objects.all()
    urun = Urun.objects.filter(kategori_id=id)

    c = {"kategori": kategori,
         "footer": footer,
         "urun": urun,
         'request': request}
    return render(request, "home/shop.html", c)

def productdetail(request, id):
    footer = Footer.objects.all()
    kategori = Kategori.objects.all()
    detail = Urun.objects.filter(id=id)
    c={"detail": detail,
       "kategori": kategori,
       "footer": footer}
    return render(request, "home/productdetail.html", c)

def colors(request):
    footer = Footer.objects.all()
    kategori = Kategori.objects.all()
    renk = Renkler.objects.all()

    c = {"kategori": kategori,
         "footer": footer,
         "renk": renk}

    return render(request, "home/colors.html", c)

def aboutus(request):
    footer = Footer.objects.all()
    kategori = Kategori.objects.all()
    hakkimizda = Hakkimizda.objects.all()

    c = {"kategori": kategori,
         "footer": footer,
         "hakkimizda": hakkimizda}
    return render(request, "home/aboutus.html", c)

def contactus(request):
    return render(request, "home/contactus.html")
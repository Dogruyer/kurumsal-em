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
    tumu = Kategori.objects.all()
    c = {"tumu": tumu}
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
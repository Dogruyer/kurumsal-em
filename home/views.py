# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render_to_response,render,HttpResponse
from django.core.context_processors import csrf

from django.shortcuts import render

def home(request):
    return render(request, "home/index.html")

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
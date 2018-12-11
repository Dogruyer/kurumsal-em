# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    return render(request, "panel/index.html")

def altkategoriresimtablo(request):
    return render(request, "panel/altkategoriresimtablo.html")

def anakategorilertablo(request):
    return render(request, "panel/anakategorilertablo.html")

def anasayfakategoritablo(request):
    return render(request, "panel/anakategorilertablo.html")

def basicform(request):
    return render(request, "panel/basicform.html")

def blogtablo(request):
    return render(request, "panel/blogtablo.html")

def footertablo(request):
    return render(request, "panel/footertablo.html")

def hakkimizdatablo(request):
    return render(request, "panel/hakkimizdatablo.html")

def iletisimform(request):
    return render(request, "panel/iletisimform.html")

def iletisimtablo(request):
    return render(request, "panel/iletisimtablo.html")

def karttablo(request):
    return render(request, "panel/karttablo.html")

def kategoribannertablo(request):
    return render(request, "panel/kategoribannertablo.html")

def koleksiyontablo(request):
    return render(request, "panel/koleksiyontablo.html")

def onecikanlartablo(request):
    return render(request, "panel/onecikanlartablo.html")

def renklertablo(request):
    return render(request, "panel/renklertablo.html")

def slidertablo(request):
    return render(request, "panel/slidertablo.html")

def uploadform(request):
    return render(request, "panel/uploadform.html")

def altkategorilerresim(request):
    return render(request, "panel/altkategorilerresim.html")


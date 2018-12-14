from django.shortcuts import render, HttpResponse
from .forms import *
from .models import *
from django.core.context_processors import csrf

#
# def index(request):
#     return render(request, "panel/index.html")
#
# def altkategoriresimtablo(request):
#     return render(request, "panel/altkategoriresimtablo.html")
#
# def anakategorilertablo(request):
#     return render(request, "panel/anakategorilertablo.html")
#
# def anasayfakategoritablo(request):
#     return render(request, "panel/anakategorilertablo.html")


def bannerekle(request):
    if request.POST:
        form = YeniBannerForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return HttpResponse("Basarili")

    form = YeniBannerForm()

    c = {"form": form,
         "request": request}

    c.update(csrf(request))

    return render(request, "panel/ornekform.html", c)


def tumbannerlar(request):
    tumu = Banner.objects.all()
    c = {"tumu": tumu}

    return render(request, "panel/renklertablo.html", c)


def basicform(request):
    if request.POST:

        form = BasicForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponse("Basarili")

    form = BasicForm()

    c = {"form": form,
         "request": request}

    c.update(csrf(request))

    return render(request, "panel/basicform.html", c)


def maillerigoster(request):
    tumu = Mail.objects.all()

    c = {"tumu" : tumu}

    return render(request, "panel/renklertablo.html", c)


def bannerduzenle(request, id):
    duzenlenecek = Banner.objects.get(id=id)

    adi = duzenlenecek.title
    gorseli = duzenlenecek.banner_image

    if request.POST:
        duzenlenecek.title = request.POST["title"]
        duzenlenecek.banner_image = request.FILES["banner_image"]

        duzenlenecek.save()

        return HttpResponse("basarili")

    # form = YeniBannerForm(initial={'title': duzenlenecek.title,
    #                                'banner_image': duzenlenecek.banner_image})

    c = {"adi": adi,
         "gorseli": gorseli}

    return render(request, "panel/duzenleform.html", c)


def sil(request, id):
    duzenlenecek = Banner.objects.get(id=id)
    duzenlenecek.delete()

    return HttpResponse("silindi")

# def blogtablo(request):
#     return render(request, "panel/blogtablo.html")
#
# def footertablo(request):
#     return render(request, "panel/footertablo.html")
#
# def hakkimizdatablo(request):
#     return render(request, "panel/hakkimizdatablo.html")
#
# def iletisimform(request):
#     return render(request, "panel/iletisimform.html")
#
# def iletisimtablo(request):
#     return render(request, "panel/iletisimtablo.html")
#
# def karttablo(request):
#     return render(request, "panel/karttablo.html")
#
# def kategoribannertablo(request):
#     return render(request, "panel/kategoribannertablo.html")
#
# def koleksiyontablo(request):
#     return render(request, "panel/koleksiyontablo.html")
#
# def onecikanlartablo(request):
#     return render(request, "panel/onecikanlartablo.html")
#
# def renklertablo(request):
#     return render(request, "panel/renklertablo.html")

def slidertablo(request):




    return render(request, "panel/slidertablo.html")

# def uploadform(request):
#     return render(request, "panel/uploadform.html")
#
# def altkategorilerresim(request):
#     return render(request, "panel/altkategorilerresim.html")


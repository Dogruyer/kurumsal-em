from django.shortcuts import render, HttpResponse
from .forms import *
from .models import *
from django.core.context_processors import csrf


def index(request):
    return render(request, "panel/index.html")

def slidertablo(request):
    tumu = Slider.objects.all()
    c = {"tumu": tumu}

    return render(request, "panel/slidertablo.html", c)

def slaytekle(request):
    if request.POST:
        form = YeniSliderForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return HttpResponse("Basarili")

    form = YeniSliderForm()

    c = {"form": form,
         "request": request}

    c.update(csrf(request))

    return render(request, "panel/slaytekle.html", c)

def slaytduzenle(request, id):
    duzenlenecek = Slider.objects.get(id=id)

    gorseli = duzenlenecek.slider_image

    if request.POST:
        duzenlenecek.slider_image = request.FILES["slider_image"]

        duzenlenecek.save()

        return HttpResponse("basarili")

    # form = YeniBannerForm(initial={'title': duzenlenecek.title,
    #                                'banner_image': duzenlenecek.banner_image})

    c = {"gorseli": gorseli}

    return render(request, "panel/slaytduzenle.html", c)

def slaytsil(request, id):
    duzenlenecek = Slider.objects.get(id=id)
    duzenlenecek.delete()



def altkategoriresimtablo(request):
    tumu = Kategori.objects.all()
    c = {"tumu": tumu}
    return render(request, "panel/altkategoriresimtablo.html")

def altkategoriresimrekle(request):
    if request.POST:
        form = Yenialtkategoriresimtablo(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return HttpResponse("Basarili")

    form = Yenialtkategoriresimtablo()

    c = {"form": form,
         "request": request}

    c.update(csrf(request))

    return render(request, "panel/altkategoriresimrekle.html", c)

def altkategoriresimduzenle(request, id):
    duzenlenecek = Kategori.objects.get(id=id)

    adi = duzenlenecek.title
    gorseli = duzenlenecek.kategori_image

    if request.POST:
        duzenlenecek.title = request.POST["title"]
        duzenlenecek.kategori_image = request.FILES["kategori_image"]

        duzenlenecek.save()

        return HttpResponse("basarili")

    # form = YeniBannerForm(initial={'title': duzenlenecek.title,
    #                                'banner_image': duzenlenecek.banner_image})

    c = {"adi": adi,
         "gorseli": gorseli}

    return render(request, "panel/duzenleform.html", c)

def altkategoriresimsil(request, id):
    duzenlenecek = Kategori.objects.get(id=id)
    duzenlenecek.delete()

    return HttpResponse("silindi")




def koleksiyontablo(request):
    tumu = Koleksiyonlar.objects.all()
    c = {"tumu": tumu}
    return render(request, "panel/koleksiyontablo.html")

def koleksiyonekle(request):
    if request.POST:
        form = Yenikoleksiyontablo(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return HttpResponse("Basarili")

    form = Yenikoleksiyontablo()

    c = {"form": form,
         "request": request}

    c.update(csrf(request))

    return render(request, "panel/koleksiyonekle.html", c)

def koleksiyonduzenle(request, id):
    duzenlenecek = Koleksiyonlar.objects.get(id=id)

    adi = duzenlenecek.title
    gorseli = duzenlenecek.koleksiyon_image
    content = duzenlenecek.content

    if request.POST:
        duzenlenecek.title = request.POST["title"]
        duzenlenecek.content = request.POST["content"]
        duzenlenecek.koleksiyon_image = request.FILES["koleksiyon_image"]

        duzenlenecek.save()

        return HttpResponse("basarili")

    # form = YeniBannerForm(initial={'title': duzenlenecek.title,
    #                                'banner_image': duzenlenecek.banner_image})

    c = {"adi": adi,
         "gorseli": gorseli,
         "icerik" : content}

    return render(request, "panel/duzenleform.html", c)

def koleksiyonsil(request, id):
    duzenlenecek = Koleksiyonlar.objects.get(id=id)
    duzenlenecek.delete()

    return HttpResponse("silindi")



def karttablo(request):
    tumu = Kartlar.objects.all()
    c = {"tumu": tumu}
    return render(request, "panel/karttablo.html")

def kartekle(request):
    if request.POST:
        form = Yenikarttablo(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return HttpResponse("Basarili")

    form = Yenikarttablo()

    c = {"form": form,
         "request": request}

    c.update(csrf(request))

    return render(request, "panel/kartekle.html", c)

def kartduzenle(request, id):
    duzenlenecek = Kartlar.objects.get(id=id)

    adi = duzenlenecek.title
    gorseli = duzenlenecek.kart_image

    if request.POST:
        duzenlenecek.title = request.POST["title"]
        duzenlenecek.kart_image = request.FILES["kart_image"]

        duzenlenecek.save()

        return HttpResponse("basarili")

    # form = YeniBannerForm(initial={'title': duzenlenecek.title,
    #                                'banner_image': duzenlenecek.banner_image})

    c = {"adi": adi,
         "gorseli": gorseli}

    return render(request, "panel/duzenleform.html", c)

def kartsil(request, id):
    duzenlenecek = Kartlar.objects.get(id=id)
    duzenlenecek.delete()

    return HttpResponse("silindi")




def blogtablo(request):
    tumu = Blog.objects.all()
    c = {"tumu": tumu}
    return render(request, "panel/blogtablo.html")

def blogekle(request):
    if request.POST:
        form = Yeniblogtablo(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return HttpResponse("Basarili")

    form = Yeniblogtablo()

    c = {"form": form,
         "request": request}

    c.update(csrf(request))

    return render(request, "panel/blogekle.html", c)

def blogduzenle(request, id):
    duzenlenecek = Blog.objects.get(id=id)

    adi = duzenlenecek.title
    content = duzenlenecek.content
    gorseli = duzenlenecek.blog_image

    if request.POST:
        duzenlenecek.title = request.POST["title"]
        duzenlenecek.content = request.POST["content"]
        duzenlenecek.blog_image = request.FILES["blog_image"]

        duzenlenecek.save()

        return HttpResponse("basarili")

    # form = YeniBannerForm(initial={'title': duzenlenecek.title,
    #                                'banner_image': duzenlenecek.banner_image})

    c = {"adi": adi,
         "gorseli": gorseli,
         "content": content}

    return render(request, "panel/duzenleform.html", c)

def blogsil(request, id):
    duzenlenecek = Blog.objects.get(id=id)
    duzenlenecek.delete()

    return HttpResponse("silindi")






def footertablo(request):
    tumu = Footer.objects.all()
    c = {"tumu": tumu}
    return render(request, "panel/footertablo.html")

def footerekle(request):
    if request.POST:
        form = Yenifootertablo(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return HttpResponse("Basarili")

    form = Yenifootertablo()

    c = {"form": form,
         "request": request}

    c.update(csrf(request))

    return render(request, "panel/footerekle.html", c)

def footerduzenle(request, id):
    duzenlenecek = Blog.objects.get(id=id)

    slogan = duzenlenecek.slogan
    adres = duzenlenecek.adres
    telefon = duzenlenecek.telefon
    email = duzenlenecek.email

    if request.POST:
        duzenlenecek.slogan = request.POST["slogan"]
        duzenlenecek.adres = request.POST["adres"]
        duzenlenecek.telefon = request.POST["telefon"]
        duzenlenecek.email = request.POST["email"]

        duzenlenecek.save()

        return HttpResponse("basarili")

    # form = YeniBannerForm(initial={'title': duzenlenecek.title,
    #                                'banner_image': duzenlenecek.banner_image})

    c = {"slogan": slogan,
         "adres": adres,
         "telefon": telefon,
         "email": email}

    return render(request, "panel/duzenleform.html", c)

def footersil(request, id):
    duzenlenecek = Footer.objects.get(id=id)
    duzenlenecek.delete()

    return HttpResponse("silindi")





def kategoribannertablo(request):
    tumu = Urun.objects.all()
    c = {"tumu": tumu}
    return render(request, "panel/kategoribannertablo.html")

def kategoribannerekle(request):
    if request.POST:
        form = Yenikategoribannertablo(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return HttpResponse("Basarili")

    form = Yenikategoribannertablo()

    c = {"form": form,
         "request": request}

    c.update(csrf(request))

    return render(request, "panel/kategoribannerekle.html", c)

def kategoribannerduzenle(request, id):
    duzenlenecek = Urun.objects.get(id=id)

    adi = duzenlenecek.title
    content = duzenlenecek.content
    gorseli = duzenlenecek.urun_image

    if request.POST:
        duzenlenecek.title = request.POST["title"]
        duzenlenecek.content = request.POST["content"]
        duzenlenecek.urun_image = request.FILES["urun_image"]

        duzenlenecek.save()

        return HttpResponse("basarili")

    # form = YeniBannerForm(initial={'title': duzenlenecek.title,
    #                                'banner_image': duzenlenecek.banner_image})

    c = {"adi": adi,
         "gorseli": gorseli,
         "content": content}

    return render(request, "panel/duzenleform.html", c)

def kategoribannersil(request, id):
    duzenlenecek = Urun.objects.get(id=id)
    duzenlenecek.delete()

    return HttpResponse("silindi")





def renklertablo(request):
    tumu = Renkler.objects.all()
    c = {"tumu": tumu}
    return render(request, "panel/renklertablo.html")

def renklerekle(request):
    if request.POST:
        form = Yenirenklertablo(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return HttpResponse("Basarili")

    form = Yenirenklertablo()

    c = {"form": form,
         "request": request}

    c.update(csrf(request))

    return render(request, "panel/renklerekle.html", c)

def renklerduzenle(request, id):
    duzenlenecek = Renkler.objects.get(id=id)

    adi = duzenlenecek.title
    gorseli = duzenlenecek.renk_image

    if request.POST:
        duzenlenecek.title = request.POST["title"]
        duzenlenecek.renk_image = request.FILES["renk_image"]

        duzenlenecek.save()

        return HttpResponse("basarili")

    # form = YeniBannerForm(initial={'title': duzenlenecek.title,
    #                                'banner_image': duzenlenecek.banner_image})

    c = {"adi": adi,
         "gorseli": gorseli}

    return render(request, "panel/duzenleform.html", c)

def renklersil(request, id):
    duzenlenecek = Renkler.objects.get(id=id)
    duzenlenecek.delete()

    return HttpResponse("silindi")




def hakkimizdatablo(request):
    tumu = Hakkimizda.objects.all()
    c = {"tumu": tumu}
    return render(request, "panel/hakkimizdatablo.html")

def hakkimizdaekle(request):
    if request.POST:
        form = Yenihakkimizdatablo(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return HttpResponse("Basarili")

    form = Yenihakkimizdatablo()

    c = {"form": form,
         "request": request}

    c.update(csrf(request))

    return render(request, "panel/hakkimizdaekle.html", c)

def hakkimizdaduzenle(request, id):
    duzenlenecek = Hakkimizda.objects.get(id=id)

    title = duzenlenecek.title
    content = duzenlenecek.content
    hakkimizda_gorsel = duzenlenecek.hakkimizda_gorsel
    sayfa_gorseli = duzenlenecek.sayfa_gorseli

    if request.POST:
        duzenlenecek.title = request.POST["title"]
        duzenlenecek.content = request.POST["content"]
        duzenlenecek.hakkimizda_gorsel = request.FILES["hakkimizda_gorsel"]
        duzenlenecek.sayfa_gorseli = request.FILES["sayfa_gorseli"]

        duzenlenecek.save()

        return HttpResponse("basarili")

    # form = YeniBannerForm(initial={'title': duzenlenecek.title,
    #                                'banner_image': duzenlenecek.banner_image})

    c = {"title": title,
         "content": content,
         "hakkimizda_gorsel": hakkimizda_gorsel,
         "sayfa_gorseli": sayfa_gorseli}

    return render(request, "panel/duzenleform.html", c)

def hakkimizdasil(request, id):
    duzenlenecek = Hakkimizda.objects.get(id=id)
    duzenlenecek.delete()

    return HttpResponse("silindi")












def anakategorilertablo(request):
    return render(request, "panel/anakategorilertablo.html")

def anasayfakategoritablo(request):
    return render(request, "panel/anakategorilertablo.html")


def iletisimform(request):
    return render(request, "panel/iletisimform.html")

def iletisimtablo(request):
    return render(request, "panel/iletisimtablo.html")


def onecikanlartablo(request):
    return render(request, "panel/onecikanlartablo.html")


def uploadform(request):
    return render(request, "panel/uploadform.html")

def altkategorilerresim(request):
    return render(request, "panel/altkategorilerresim.html")





def tumbannerlar(request):
    tumu = Banner.objects.all()
    c = {"tumu": tumu}

    return render(request, "panel/renklertablo.html", c)

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


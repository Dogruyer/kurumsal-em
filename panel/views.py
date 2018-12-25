from django.shortcuts import render, HttpResponse, render_to_response, redirect
from django.core.urlresolvers import reverse
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

            return redirect(reverse(slidertablo))

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

        return redirect(reverse(slidertablo))

    c = {"gorseli": gorseli}

    return render(request, "panel/slaytduzenle.html", c)

def slaytsil(request, id):
    duzenlenecek = Slider.objects.get(id=id)
    duzenlenecek.delete()

    return redirect(reverse(slidertablo))



def altkategoriresimtablo(request):
    tumu = Kategori_bolumu.objects.all()
    c = {"tumu": tumu}
    return render(request, "panel/altkategoriresimtablo.html", c)

def altkategoriresimekle(request):
    if request.POST:
        form = Yenialtkategoriresimtablo(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect(reverse(altkategoriresimtablo))

    form = Yenialtkategoriresimtablo()

    c = {"form": form,
         "request": request}

    c.update(csrf(request))

    return render(request, "panel/altkategoriresimekle.html", c)

def altkategoriresimduzenle(request, id):
    duzenlenecek = Kategori_bolumu.objects.get(id=id)

    adi = duzenlenecek.title
    gorseli = duzenlenecek.kategori_image

    if request.POST:
        duzenlenecek.title = request.POST["title"]
        duzenlenecek.kategori_image = request.FILES["kategori_image"]

        duzenlenecek.save()

        return redirect(reverse(altkategoriresimtablo))

    c = {"adi": adi,
         "gorseli": gorseli}

    return render(request, "panel/altkategoriresimduzenle.html", c)

def altkategoriresimsil(request, id):
    duzenlenecek = Kategori_bolumu.objects.get(id=id)
    duzenlenecek.delete()

    return redirect(reverse(altkategoriresimtablo))


def kategoritablo(request):
    tumu = Kategori.objects.all()
    c = {"tumu": tumu}
    return render(request, "panel/kategoritablo.html", c)

def kategoriekle(request):
    if request.POST:
        form = YeniKategoriForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect(reverse(kategoritablo))

    form = YeniKategoriForm()

    c = {"form": form,
         "request": request}

    c.update(csrf(request))

    return render(request, "panel/kategoriekle.html", c)

def kategoriduzenle(request, id):
    duzenlenecek = Kategori.objects.get(id=id)

    adi = duzenlenecek.title

    if request.POST:
        duzenlenecek.title = request.POST["title"]

        duzenlenecek.save()

        return redirect(reverse(kategoritablo))

    c = {"adi": adi}

    return render(request, "panel/kategoriduzenle.html", c)

def kategorisil(request, id):
    duzenlenecek = Kategori.objects.get(id=id)
    duzenlenecek.delete()

    return redirect(reverse(kategoritablo))



def koleksiyonkategoritablo(request):
    tumu = KoleksiyonKategori.objects.all()
    c = {"tumu": tumu}
    return render(request, "panel/koleksiyonkategoritablo.html", c)

def koleksiyonkategoriekle(request):
    if request.POST:
        form = YeniKoleksiyonKategoriForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect(reverse(koleksiyonkategoritablo))

    form = YeniKoleksiyonKategoriForm()

    c = {"form": form,
         "request": request}

    c.update(csrf(request))

    return render(request, "panel/koleksiyonkategoriekle.html", c)

def koleksiyonkategoriduzenle(request, id):
    duzenlenecek = KoleksiyonKategori.objects.get(id=id)

    adi = duzenlenecek.title

    if request.POST:
        duzenlenecek.title = request.POST["title"]

        duzenlenecek.save()

        return redirect(reverse(koleksiyonkategoritablo))

    c = {"adi": adi}

    return render(request, "panel/koleksiyonkategoriduzenle.html", c)

def koleksiyonkategorisil(request, id):
    duzenlenecek = KoleksiyonKategori.objects.get(id=id)
    duzenlenecek.delete()

    return redirect(reverse(koleksiyonkategoritablo))



def koleksiyontablo(request):
    tumu = Koleksiyonlar.objects.all()
    c = {"tumu": tumu}
    return render(request, "panel/koleksiyontablo.html", c)

def koleksiyonekle(request):
    tumkategoriler = KoleksiyonKategori.objects.all()
    if request.POST:
        form = Yenikoleksiyontablo(request.POST, request.FILES)
        koleksiyonkategori = request.POST["koleksiyonkategori"]
        kategori_nesne = KoleksiyonKategori.objects.get(id=koleksiyonkategori)


        if form.is_valid():
            yeni = Koleksiyonlar()
            yeni.title = form.cleaned_data.get('title')
            yeni.content = form.cleaned_data.get('content')
            yeni.image = form.cleaned_data.get('koleksiyon_image')
            yeni.koleksiyonkategori = kategori_nesne
            yeni.save()

            return redirect(reverse(koleksiyontablo))

    form = Yenikoleksiyontablo()

    c = {"form": form,
         "tumkategoriler" : tumkategoriler,
         "request": request}

    c.update(csrf(request))

    return render(request, "panel/koleksiyonekle.html", c)

def koleksiyonduzenle(request, id):
    duzenlenecek = Koleksiyonlar.objects.get(id=id)
    tumu = KoleksiyonKategori.objects.get()
    adi = duzenlenecek.title
    gorseli = duzenlenecek.koleksiyon_image
    content = duzenlenecek.content
    kategori = duzenlenecek.koleksiyonkategori.title

    if request.POST:
        duzenlenecek.title = request.POST["title"]
        duzenlenecek.content = request.POST["content"]
        duzenlenecek.koleksiyon_image = request.FILES["koleksiyon_image"]
        duzenlenecek.koleksiyonkategori = request.POST["koleksiyonkategori.title "]

        duzenlenecek.save()

        return redirect(reverse(koleksiyontablo))

    c = {"adi": adi,
         "gorseli": gorseli,
         "tumu" : tumu,
         "kategori" : kategori,
         "icerik" : content}

    return render(request, "panel/koleksiyonduzenle.html", c)

def koleksiyonsil(request, id):
    duzenlenecek = Koleksiyonlar.objects.get(id=id)
    duzenlenecek.delete()

    return redirect(reverse(koleksiyontablo))



def karttablo(request):
    tumu = Kartlar.objects.all()
    c = {"tumu": tumu}
    return render(request, "panel/karttablo.html", c)

def kartekle(request):
    if request.POST:
        form = Yenikarttablo(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect(reverse(karttablo))

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

        return redirect(reverse(karttablo))

    c = {"adi": adi,
         "gorseli": gorseli}

    return render(request, "panel/kartduzenle.html", c)

def kartsil(request, id):
    duzenlenecek = Kartlar.objects.get(id=id)
    duzenlenecek.delete()

    return redirect(reverse(karttablo))




def blogtablo(request):
    tumu = Blog.objects.all()
    c = {"tumu": tumu}
    return render(request, "panel/blogtablo.html", c)

def blogekle(request):
    if request.POST:
        form = Yeniblogtablo(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect(reverse(blogtablo))

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

        return redirect(reverse(blogtablo))

    c = {"adi": adi,
         "gorseli": gorseli,
         "content": content}

    return render(request, "panel/blogduzenle.html", c)

def blogsil(request, id):
    duzenlenecek = Blog.objects.get(id=id)
    duzenlenecek.delete()

    return redirect(reverse(blogtablo))





def footertablo(request):
    tumu = Footer.objects.all()
    c = {"tumu": tumu}
    return render(request, "panel/footertablo.html", c)

def footerekle(request):
    if request.POST:
        form = Yenifootertablo(request.POST)

        if form.is_valid():
            form.save()

            return redirect(reverse(footertablo))

    form = Yenifootertablo()

    c = {"form": form,
         "request": request}

    c.update(csrf(request))

    return render(request, "panel/footerekle.html", c)

def footerduzenle(request, id):
    duzenlenecek = Footer.objects.get(id=id)

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

        return redirect(reverse(footertablo))


    c = {"slogan": slogan,
         "adres": adres,
         "telefon": telefon,
         "email": email}

    return render(request, "panel/footerduzenle.html", c)

def footersil(request, id):
    duzenlenecek = Footer.objects.get(id=id)
    duzenlenecek.delete()

    return redirect(reverse(footertablo))





def kategoribannertablo(request):
    tumu = Urun.objects.all()
    c = {"tumu": tumu}
    return render(request, "panel/kategoribannertablo.html",c)

def kategoribannerekle(request):
    tumkategoriler = Kategori.objects.all()
    if request.POST:
        form = Yenikategoribannertablo(request.POST, request.FILES)
        kategori = request.POST["kategori"]
        kategori_getir = Kategori.objects.get(id=kategori)

        if form.is_valid():
            yeni = Urun()
            yeni.title = form.cleaned_data.get('title')
            yeni.content = form.cleaned_data.get('content')
            yeni.urun_image = request.FILES["urun_image"]
            yeni.kategori_id = kategori_getir
            yeni.save()


            return redirect(reverse(kategoribannertablo))

    form = Yenikategoribannertablo()

    c = {"form": form,
         "tumkategoriler" : tumkategoriler,
         "request": request}

    c.update(csrf(request))

    return render(request, "panel/kategoribannerekle.html", c)

def kategoribannerduzenle(request, id):
    tumkategoriler = Kategori.objects.all()
    duzenlenecek = Urun.objects.get(id=id)

    adi = duzenlenecek.title
    content = duzenlenecek.content
    gorseli = duzenlenecek.urun_image
    kategori = tumkategoriler.title

    if request.POST:
        duzenlenecek.title = request.POST["title"]
        duzenlenecek.content = request.POST["content"]
        duzenlenecek.urun_image = request.FILES["urun_image"]
        duzenlenecek.save()

        return redirect(reverse(kategoribannertablo))
    c = {"adi": adi,
         "kategori": kategori,
         "gorseli": gorseli,
         "content": content}

    return render(request, "panel/kategoribannerduzenle.html", c)

def kategoribannersil(request, id):
    duzenlenecek = Urun.objects.get(id=id)
    duzenlenecek.delete()

    return redirect(reverse(kategoribannertablo))





def renklertablo(request):
    tumu = Renkler.objects.all()
    c = {"tumu": tumu}
    return render(request, "panel/renklertablo.html", c)

def renklerekle(request):
    if request.POST:
        form = Yenirenklertablo(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect(reverse(renklertablo))

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

        return redirect(reverse(renklertablo))

    # form = YeniBannerForm(initial={'title': duzenlenecek.title,
    #                                'banner_image': duzenlenecek.banner_image})

    c = {"adi": adi,
         "gorseli": gorseli}

    return render(request, "panel/renklerduzenle.html", c)

def renklersil(request, id):
    duzenlenecek = Renkler.objects.get(id=id)
    duzenlenecek.delete()

    return redirect(reverse(renklertablo))




def hakkimizdatablo(request):
    tumu = Hakkimizda.objects.all()
    c = {"tumu": tumu}
    return render(request, "panel/hakkimizdatablo.html", c)

def hakkimizdaekle(request):
    if request.POST:
        form = Yenihakkimizdatablo(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect(reverse(hakkimizdatablo))

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

        return redirect(reverse(hakkimizdatablo))


    c = {"title": title,
         "content": content,
         "hakkimizda_gorsel": hakkimizda_gorsel,
         "sayfa_gorseli": sayfa_gorseli}

    return render(request, "panel/hakkimizdaduzenle.html", c)

def hakkimizdasil(request, id):
    duzenlenecek = Hakkimizda.objects.get(id=id)
    duzenlenecek.delete()

    return redirect(reverse(hakkimizdatablo))



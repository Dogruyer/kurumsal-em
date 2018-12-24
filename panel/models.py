from django.db import models


class Slider(models.Model):
    slider_image = models.ImageField(upload_to='images/slider/',
                                     default='images/slider/default.jpg')
class Kategori(models.Model):
    title = models.CharField(max_length=100)

class KoleksiyonKategori(models.Model):
    title = models.CharField(max_length=100)

class Kategori_bolumu(models.Model):
    title = models.CharField(max_length=100)
    kategori_image = models.ImageField(upload_to='images/kategori/',
                              default='images/kategori/default.jpg')

class Koleksiyonlar(models.Model):
    koleksiyon_image = models.ImageField(upload_to='images/koleksiyonlar/',
                                          default='images/koleksiyonlar/default.jpg')
    koleksiyonkategori = models.ForeignKey(KoleksiyonKategori)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)


class Kartlar(models.Model):
    kart_image = models.ImageField(upload_to='images/kartlar/',
                                   default='images/kartlar/default.jpg')
    title = models.CharField(max_length=100)


# sonra acilacak
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    blog_image = models.ImageField(upload_to='images/blog/',
                                   default='images/blog/default.jpg')


class Footer(models.Model):
    slogan = models.CharField(max_length=100)
    adres = models.CharField(max_length=100)
    telefon = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)


class Urun(models.Model):
    urun_image = models.ImageField(upload_to='images/urun/',
                                   default='images/urun/default.jpg')
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    kategori_id = models.ForeignKey(Kategori)


class Renkler(models.Model):
    renk_image = models.ImageField(upload_to='images/renkler/',
                                   default='images/renkler/default.jpg')
    title = models.CharField(max_length=100)


class Hakkimizda(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    hakkimizda_gorsel = models.ImageField(upload_to='images/hakkimizda/',
                                          default='images/hakkimizda/default.jpg')
    sayfa_gorseli = models.ImageField(upload_to='images/hakkimizda/',
                                      default='images/hakkimizda/default.jpg')


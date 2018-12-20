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
    koleksiyon_image = models.ImageField(upload_to='static/images/koleksiyonlar/',
                                          default='static/images/koleksiyonlar/default.jpg')
    koleksiyonkategori = models.ForeignKey(KoleksiyonKategori)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)


class Kartlar(models.Model):
    kart_image = models.ImageField(upload_to='static/images/kartlar/',
                                   default='static/images/kartlar/default.jpg')
    title = models.CharField(max_length=100)


# sonra acilacak
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    blog_image = models.ImageField(upload_to='static/images/blog/',
                                   default='static/images/blog/default.jpg')


class Footer(models.Model):
    slogan = models.CharField(max_length=100)
    adres = models.CharField(max_length=100)
    telefon = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)


class Urun(models.Model):
    urun_image = models.ImageField(upload_to='static/images/urun/',
                                   default='static/images/urun/default.jpg')
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    kategori_id = models.ForeignKey(Kategori)


class Renkler(models.Model):
    renk_image = models.ImageField(upload_to='static/images/renkler/',
                                   default='static/images/renkler/default.jpg')
    title = models.CharField(max_length=100)


class Hakkimizda(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    hakkimizda_gorsel = models.ImageField(upload_to='static/images/hakkimizda/',
                                          default='static/images/hakkimizda/default.jpg')
    sayfa_gorseli = models.ImageField(upload_to='static/images/hakkimizda/',
                                      default='static/images/hakkimizda/default.jpg')

class Banner(models.Model):
    title = models.CharField(max_length=100)
    banner_image = models.ImageField(upload_to='static/images/banner/',
                                     default='static/images/banner/default.jpg')

class Mail(models.Model):
    email = models.EmailField(max_length=200)

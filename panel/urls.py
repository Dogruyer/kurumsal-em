from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

                       url(r'^$',
                           'panel.views.index',
                           name='index'),

                       url(r'^slidertablo$',
                           'panel.views.slidertablo',
                           name='slidertablo'),

                       url(r'^slaytekle$',
                           'panel.views.slaytekle',
                           name='slaytekle'),

                       url(r'^slaytduzenle/(?P<id>\w+)$',
                           'panel.views.slaytduzenle',
                           name='slaytduzenle'),

                       url(r'^slaytsil/(?P<id>\w+)$',
                           'panel.views.slaytsil',
                           name='slaytsil'),



                       url(r'^kategoritablo$',
                           'panel.views.kategoritablo',
                           name='kategoritablo'),

                       url(r'^kategoriekle$',
                           'panel.views.kategoriekle',
                           name='kategoriekle'),

                       url(r'^kategoriduzenle/(?P<id>\w+)$',
                           'panel.views.kategoriduzenle',
                           name='kategoriduzenle'),

                       url(r'^kategorisil/(?P<id>\w+)$',
                           'panel.views.kategorisil',
                           name='kategorisil'),



                       url(r'^koleksiyonkategoritablo$',
                           'panel.views.koleksiyonkategoritablo',
                           name='koleksiyonkategoritablo'),

                       url(r'^koleksiyonkategoriekle$',
                           'panel.views.koleksiyonkategoriekle',
                           name='koleksiyonkategoriekle'),

                       url(r'^koleksiyonkategoriduzenle/(?P<id>\w+)$',
                           'panel.views.koleksiyonkategoriduzenle',
                           name='koleksiyonkategoriduzenle'),

                       url(r'^koleksiyonkategorisil/(?P<id>\w+)$',
                           'panel.views.koleksiyonkategorisil',
                           name='koleksiyonkategorisil'),




                       url(r'^altkategoriresimtablo$',
                           'panel.views.altkategoriresimtablo',
                           name='altkategoriresimtablo'),

                       url(r'^altkategoriresimekle',
                           'panel.views.altkategoriresimekle',
                           name='altkategoriresimekle'),

                       url(r'^altkategoriresimduzenle/(?P<id>\w+)$',
                           'panel.views.altkategoriresimduzenle',
                           name='altkategoriresimduzenle'),

                       url(r'^altkategoriresimsil/(?P<id>\w+)$',
                           'panel.views.altkategoriresimsil',
                           name='altkategoriresimsil'),





                       url(r'^koleksiyontablo$',
                           'panel.views.koleksiyontablo',
                           name='koleksiyontablo'),

                       url(r'^koleksiyonekle$',
                           'panel.views.koleksiyonekle',
                           name='koleksiyonekle'),

                       url(r'^koleksiyonduzenle/(?P<id>\w+)$',
                           'panel.views.koleksiyonduzenle',
                           name='koleksiyonduzenle'),

                       url(r'^koleksiyonsil/(?P<id>\w+)$',
                           'panel.views.koleksiyonsil',
                           name='koleksiyonsil'),






                       url(r'^karttablo$',
                           'panel.views.karttablo',
                           name='karttablo'),

                       url(r'^kartekle$',
                           'panel.views.kartekle',
                           name='kartekle'),

                       url(r'^kartduzenle/(?P<id>\w+)$',
                           'panel.views.kartduzenle',
                           name='kartduzenle'),

                       url(r'^kartsil/(?P<id>\w+)$',
                           'panel.views.kartsil',
                           name='kartsil'),






                       url(r'^blogtablo$',
                           'panel.views.blogtablo',
                           name='blogtablo'),

                       url(r'^blogekle$',
                           'panel.views.blogekle',
                           name='blogekle'),

                       url(r'^blogduzenle/(?P<id>\w+)$',
                           'panel.views.blogduzenle',
                           name='blogduzenle'),

                       url(r'^blogsil/(?P<id>\w+)$',
                           'panel.views.blogsil',
                           name='blogsil'),





                       url(r'^footertablo$',
                           'panel.views.footertablo',
                           name='footertablo'),

                       url(r'^footerekle$',
                           'panel.views.footerekle',
                           name='footerekle'),

                       url(r'^footerduzenle/(?P<id>\w+)$',
                           'panel.views.footerduzenle',
                           name='footerduzenle'),

                       url(r'^footersil/(?P<id>\w+)$',
                           'panel.views.footersil',
                           name='footersil'),








                       url(r'^kategoribannertablo$',
                           'panel.views.kategoribannertablo',
                           name='kategoribannertablo'),


                       url(r'^kategoribannerekle$',
                           'panel.views.kategoribannerekle',
                           name='kategoribannerekle'),


                       url(r'^kategoribannerduzenle/(?P<id>\w+)$',
                           'panel.views.kategoribannerduzenle',
                           name='kategoribannerduzenle'),

                       url(r'^kategoribannersil/(?P<id>\w+)$',
                           'panel.views.kategoribannersil',
                           name='kategoribannersil'),






                       url(r'^renklertablo$',
                           'panel.views.renklertablo',
                           name='renklertablo'),

                       url(r'^renklerekle$',
                           'panel.views.renklerekle',
                           name='renklerekle'),

                       url(r'^renklerduzenle/(?P<id>\w+)$',
                           'panel.views.renklerduzenle',
                           name='renklerduzenle'),

                       url(r'^renklersil/(?P<id>\w+)$',
                           'panel.views.renklersil',
                           name='renklersil'),





                       url(r'^hakkimizdatablo$',
                           'panel.views.hakkimizdatablo',
                           name='hakkimizdatablo'),

                       url(r'^hakkimizdaekle$',
                           'panel.views.hakkimizdaekle',
                           name='hakkimizdaekle'),

                       url(r'^hakkimizdaduzenle/(?P<id>\w+)$',
                           'panel.views.hakkimizdaduzenle',
                           name='hakkimizdaduzenle'),

                       url(r'^hakkimizdasil/(?P<id>\w+)$',
                           'panel.views.hakkimizdasil',
                           name='hakkimizdasil'),



                       url(r'^detailfototablo$',
                           'panel.views.detailfototablo',
                           name='detailfototablo'),

                       url(r'^detailfotoekle$',
                           'panel.views.detailfotoekle',
                           name='detailfotoekle'),

                       url(r'^detailfotoduzenle/(?P<id>\w+)$',
                           'panel.views.detailfotoduzenle',
                           name='detailfotoduzenle'),

                       url(r'^detailfotosil/(?P<id>\w+)$',
                           'panel.views.detailfotosil',
                           name='detailfotosil'),



                       url(r'^detailfeaturetablo$',
                           'panel.views.detailfeaturetablo',
                           name='detailfeaturetablo'),

                       url(r'^detailfeatureekle$',
                           'panel.views.detailfeatureekle',
                           name='detailfeatureekle'),

                       url(r'^detailfeatureduzenle/(?P<id>\w+)$',
                           'panel.views.detailfeatureduzenle',
                           name='detailfeatureduzenle'),

                       url(r'^detailfeaturesil/(?P<id>\w+)$',
                           'panel.views.detailfeaturesil',
                           name='detailfeaturesil'),




                       )

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
                            (r'^media/(?P<path>.*)$',
                             'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))

if settings.DEBUG:   # if DEBUG is True it will be served automatically
    urlpatterns += patterns('',
                            url(r'^static/(?P<path>.*)$',
                                'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
                            )
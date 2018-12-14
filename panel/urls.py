from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^altkategoriresimtablo$',
                           'panel.views.altkategoriresimtablo',
                           name='altkategoriresimtablo'),

                       url(r'^anakategorilertablo$',
                           'panel.views.anakategorilertablo',
                           name='anakategorilertablo'),

                       url(r'^anasayfakategoritablo$',
                           'panel.views.anasayfakategoritablo',
                           name='anasayfakategoritablo'),

                       url(r'^basicform$',
                           'panel.views.basicform',
                           name='basicform'),

                       url(r'^blogtablo$',
                           'panel.views.blogtablo',
                           name='blogtablo'),

                       url(r'^footertablo$',
                           'panel.views.footertablo',
                           name='footertablo'),

                       url(r'^hakkimizdatablo$',
                           'panel.views.hakkimizdatablo',
                           name='hakkimizdatablo'),

                       url(r'^iletisimform$',
                           'panel.views.iletisimform',
                           name='iletisimform'),

                       url(r'^iletisimtablo$',
                           'panel.views.iletisimtablo',
                           name='iletisimtablo'),

                       url(r'^karttablo$',
                           'panel.views.karttablo',
                           name='karttablo'),

                       url(r'^kategoribannertablo$',
                           'panel.views.kategoribannertablo',
                           name='kategoribannertablo'),

                       url(r'^koleksiyontablo$',
                           'panel.views.koleksiyontablo',
                           name='koleksiyontablo'),

                       url(r'^onecikanlartablo$',
                           'panel.views.onecikanlartablo',
                           name='onecikanlartablo'),
                       url(r'^renklertablo$',
                           'panel.views.tumbannerlar',
                           name='tumbannerlar'),

                       url(r'^slidertablo$',
                           'panel.views.slidertablo',
                           name='slidertablo'),

                       url(r'^uploadform$',
                           'panel.views.uploadform',
                           name='uploadform'),

                       url(r'^$',
                           'panel.views.index',
                           name='index'),

                       url(r'^altkategorilerresim$',
                           'panel.views.altkategorilerresim',
                           name='altkategorilerresim'),

                       url(r'^bannerekle$',
                           'panel.views.bannerekle',
                           name='bannerekle'),

                       url(r'^bannerduzenle/(?P<id>\w+)$',
                           'panel.views.bannerduzenle',
                           name='bannerduzenle'),



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
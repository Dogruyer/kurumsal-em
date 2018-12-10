from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$',
                          'home.views.home',
                          name='home'),

                       url(r'^shop$',
                          'home.views.shop',
                          name='shop'),

                       url(r'^productdetail$',
                           'home.views.productdetail',
                           name='productdetail'),

                       url(r'^colors$',
                           'home.views.colors',
                           name='colors'),

                       url(r'^aboutus$',
                           'home.views.aboutus',
                           name='aboutus'),

                       url(r'^contactus$',
                           'home.views.contactus',
                           name='contactus'),

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
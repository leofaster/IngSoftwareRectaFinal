from django.conf.urls import patterns, include, url
from views import pedirCliente, buscarFactura, buscarTodasFacturas

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ServiSoft.views.home', name='home'),
    # url(r'^ServiSoft/', include('ServiSoft.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^',include('ServiSoft.WebAccess.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

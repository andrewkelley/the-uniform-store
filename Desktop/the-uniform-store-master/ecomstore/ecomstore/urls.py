from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'preview.views.home'),
    url(r'^info/', 'preview.views.info'),    
    url(r'^', include('catalog.urls')),
    url(r'^cart/', include('cart.urls')),
    url(r'^scopes_for_the_cure/', 'preview.views.scopes_for_the_cure'),
    url(r'^james_cancer_hospital/', 'preview.views.james_cancer_hospital'),
    url(r'^mount_carmel/', 'preview.views.mount_carmel'),
    url(r'^nationwide_childrens/', 'preview.views.nationwide_childrens'),
    url(r'^ohio_health/', 'preview.views.ohio_health'),

    # url(r'^ecomstore/', include('ecomstore.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

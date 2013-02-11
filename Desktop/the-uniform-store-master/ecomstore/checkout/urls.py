from django.conf.urls.defaults import *

urlpatterns = patterns('checkout.views',
    (r'^$', 'checkout', { 'template_name': 'checkout/checkout.html' },'checkout'),
)

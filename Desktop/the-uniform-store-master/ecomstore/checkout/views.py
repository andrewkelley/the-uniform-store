from django.shortcuts import render_to_response
from django.template import RequestContext
import cart

def checkout(request, template_name="checkout/checkout.html"):
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

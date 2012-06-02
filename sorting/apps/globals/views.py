import json

from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):

    return render_to_response('base.html', {}, context_instance=RequestContext(request))

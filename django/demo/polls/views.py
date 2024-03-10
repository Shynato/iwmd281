from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

def index(request):
    context = {"adresse" : "87 Rue des embrouilles"} #variable qui sera template
    template = loader.get_template("index.html") # page web 
    return HttpResponse(template.render(context, request)) # on génère le template à partir du contexte (on garde le request)

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

def index(request):
    context = {"adresse" : "87 Rue des embrouilles"} #variable qui sera template
    template = loader.get_template("index.html") # page web 
    return HttpResponse(template.render(context, request)) # on génère le template à partir du contexte (on garde le request)

### REST API SECTION

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Todo
from .serializers import TaskSerializer


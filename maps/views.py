from __future__ import unicode_literals
from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from .models import *
from .serializers import *
import urllib, json
import requests
# Create your views here.

def farmertable(request):
    url="https://10.0.3.23:8787/farmer/?format=json"
    response=urllib.urlopen(url)
    jsondata=json.loads(response.read())
    
def farmtable(request):
    url="https://10.0.3.23:8787/farm/?format=json"
    response=urllib.urlopen(url)
    jsondata=json.loads(response.read())
    
def housetable(request):
    url="https://10.0.3.23:8787/house/?format=json"
    response=urllib.urlopen(url)
    jsondata=json.loads(response.read())
    
def members(request):
    url="https://10.0.3.23:8787/members/?format=json"
    response=urllib.urlopen(url)
    jsondata=json.loads(response.read())
    
def farmpoints(request):
    url="https://10.0.3.23:8787/farmpoints/?format=json"
    response=urllib.urlopen(url)
    jsondata=json.loads(response.read())
    
def crop(request):
    url="https://10.0.3.23:8787/crop/?format=json"
    response=urllib.urlopen(url)
    jsondata=json.loads(response.read())
    
def wells(request):
    url="https://10.0.3.23:8787/wells/?format=json"
    response=urllib.urlopen(url)
    jsondata=json.loads(response.read())
    
def publicplaces(request):
    url="https://10.0.3.23:8787/publicplaces/?format=json"
    response=urllib.urlopen(url)
    jsondata=json.loads(response.read())

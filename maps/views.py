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
    return jsondata
    
def farmtable(request):
    url="https://10.0.3.23:8787/farm/?format=json"
    response=urllib.urlopen(url)
    jsondata=json.loads(response.read())
    return jsondata
    
def housetable(request):
    url="https://10.0.3.23:8787/house/?format=json"
    response=urllib.urlopen(url)
    jsondata=json.loads(response.read())
    return jsondata
    
def memberstable(request):
    url="https://10.0.3.23:8787/members/?format=json"
    response=urllib.urlopen(url)
    jsondata=json.loads(response.read())
    return jsondata
    
def farmpointstable(request):
    url="https://10.0.3.23:8787/farmpoints/?format=json"
    response=urllib.urlopen(url)
    jsondata=json.loads(response.read())
    return jsondata
    
def croptable(request):
    url="https://10.0.3.23:8787/crop/?format=json"
    response=urllib.urlopen(url)
    jsondata=json.loads(response.read())
    return jsondata
    
def wellstable(request):
    url="https://10.0.3.23:8787/wells/?format=json"
    response=urllib.urlopen(url)
    jsondata=json.loads(response.read())
    return jsondata
    
def publicplacestable(request):
    url="https://10.0.3.23:8787/publicplaces/?format=json"
    response=urllib.urlopen(url)
    jsondata=json.loads(response.read())
    return jsondata

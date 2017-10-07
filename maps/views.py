from __future__ import unicode_literals
from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from .models import *
import urllib, json
import requests
# Create your views here.

def index(request):
    return HttpResponse('<h2>The Index of Myapp..</h2>')
    
def farmertable(request):
    url="http://10.0.3.23:8787/farmer/?format=json"
    response=urllib.urlopen(url)
    jsondata = json.loads(response.read())
    return jsondata
    
def farmtable(request):
    url="http://10.0.3.23:8787/farm/?format=json"
    response=urllib.urlopen(url)
    jsondata= json.loads(response.read())
    return jsondata
    
def housetable(request):
    url="http://10.0.3.23:8787/house/?format=json"
    response=urllib.urlopen(url)
    jsondata=json.loads(response.read())
    return jsondata
    
def memberstable(request):
    url="http://10.0.3.23:8787/members/?format=json"
    response=urllib.urlopen(url)
    jsondata=json.loads(response.read())
    return jsondata
    
def farmpointstable(request):
    url="http://10.0.3.23:8787/farmpoints/?format=json"
    response=urllib.urlopen(url)
    jsondata=json.loads(response.read())
    return jsondata
    
def croptable(request):
    url="http://10.0.3.23:8787/crop/?format=json"
    response=urllib.urlopen(url)
    jsondata=json.loads(response.read())
    return jsondata
    
def wellstable(request):
    url="http://10.0.3.23:8787/wells/?format=json"
    response=urllib.urlopen(url)
    jsondata=json.loads(response.read())
    return jsondata
    
def publicplacestable(request):
    url="http://10.0.3.23:8787/publicplaces/?format=json"
    response=urllib.urlopen(url)
    jsondata=json.loads(response.read())
    return jsondata

def mappoints(request):
    url="http://10.0.3.23:8787/farmer/?format=json"
    farmer_res=urllib.urlopen(url)
    farmerjsondata=json.loads(farmer_res.read())
    
    url="http://10.0.3.23:8787/farm/?format=json"
    farm_res=urllib.urlopen(url)
    farmjsondata=json.loads(farm_res.read())
    
    url="http://10.0.3.23:8787/house/?format=json"
    house_res=urllib.urlopen(url)
    housejsondata=json.loads(house_res.read())
    
    url="http://10.0.3.23:8787/farmpoints/?format=json"
    farmpoints_res=urllib.urlopen(url)
    farmpointsjsondata=json.loads(farmpoints_res.read())
    
    url="http://10.0.3.23:8787/members/?format=json"
    members_res=urllib.urlopen(url)
    membersjsondata=json.loads(members_res.read())
    
    url="http://10.0.3.23:8787/wells/?format=json"
    wells_res=urllib.urlopen(url)
    wellsjsondata=json.loads(wells_res.read())
    
    url="http://10.0.3.23:8787/crop/?format=json"
    crop_res=urllib.urlopen(url)
    cropjsondata=json.loads(crop_res.read())
    
    url="http://10.0.3.23:8787/farm/?format=json"
    publicplaces_res=urllib.urlopen(url)
    publicplacesjsondata=json.loads(publicplaces_res.read())
    
    return render(request, 'maps/tdmap.html', {'farmer':farmerjsondata,'farm':farmjsondata, 'house':housejsondata, 'farmpoints':farmpointsjsondata, 'wells':wellsjsondata,'publicplaces':publicplacesjsondata, 'members':membersjsondata, 'crop':cropjasondata})
    

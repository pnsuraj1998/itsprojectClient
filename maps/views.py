from __future__ import unicode_literals
from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from django.http import HttpResponse
from .models import *
import urllib, json
import requests
# Create your views here.

#GIVE INDEX PAGE
def index(request):
    return HttpResponse('<h2>The Index of Myapp..</h2>')
 
#RETRIEVE FARMER table data
def farmertable(request):
    url="http://10.0.3.23:8787/farmer/?format=json"             #GET URL INTO A STRING
    response=urllib.urlopen(url)                                #GET DATA FROM GIVEN URL
    jsondata = json.loads(response.read())                      #LOAD AS JSON DATA
    return JsonResponse(jsondata, safe=False)                   # GIVE OUT THE JSON DATA


#RETRIEVE FARM table data
def farmtable(request):
    url="http://10.0.3.23:8787/farm/?format=json"               #GET URL INTO A STRING
    response=urllib.urlopen(url)                                #GET DATA FROM GIVEN URL
    jsondata= json.loads(response.read())                       #LOAD AS JSON DATA
    return JsonResponse(jsondata, safe=False)                   # GIVE OUT THE JSON DATA


#RETRIEVE HOUSE table data
def housetable(request):
    url="http://10.0.3.23:8787/house/?format=json"              #SIMILAR TO ABOVE-
    response=urllib.urlopen(url)
    jsondata=json.loads(response.read())
    return JsonResponse(jsondata,safe=False)


#RETRIEVE MEMBERS table data
def memberstable(request):
    url="http://10.0.3.23:8787/members/?format=json"
    response=urllib.urlopen(url)
    jsondata=json.loads(response.read())
    return JsonResponse(jsondata,safe=False)


#RETRIEVE FARMPOINTS table data
def farmpointstable(request):
    url="http://10.0.3.23:8787/farmpoints/?format=json"
    response=urllib.urlopen(url)
    jsondata=json.loads(response.read())
    return JsonResponse(jsondata, safe=False)


#RETRIEVE CROP table data    
def croptable(request):
    url="http://10.0.3.23:8787/crop/?format=json"
    response=urllib.urlopen(url)
    jsondata=json.loads(response.read())
    return JsonResponse(jsondata, safe=False)
    

#RETRIEVE WELLS table data
def wellstable(request):
    url="http://10.0.3.23:8787/wells/?format=json"
    response=urllib.urlopen(url)
    jsondata=json.loads(response.read())
    return JsonResponse(jsondata, safe=False)


#RETRIEVE PUBLICPLACES table data    
def publicplacestable(request):
    url="http://10.0.3.23:8787/publicplaces/?format=json"
    response=urllib.urlopen(url)
    jsondata=json.loads(response.read())
    return JsonResponse(jsondata, safe=False)


#RETRIEVE MAP POINTS and send it to tdmap.html
def mappoints(request):
    # FARMER information
    url="http://10.0.3.23:8787/farmer/?format=json"
    farmer_res=urllib.urlopen(url)
    farmerjsondata=json.loads(farmer_res.read())
    
    # Farm information
    url="http://10.0.3.23:8787/farm/?format=json"
    farm_res=urllib.urlopen(url)
    farmjsondata=json.loads(farm_res.read())
    
    # Houses information
    url="http://10.0.3.23:8787/house/?format=json"
    house_res=urllib.urlopen(url)
    housejsondata=json.loads(house_res.read())
    
    
    # FARMPOINTS information
    url="http://10.0.3.23:8787/farmpoints/?format=json"
    farmpoints_res=urllib.urlopen(url)
    farmpointsjsondata=json.loads(farmpoints_res.read())
    
    
    # MEMBERS information
    url="http://10.0.3.23:8787/members/?format=json"
    members_res=urllib.urlopen(url)
    membersjsondata=json.loads(members_res.read())
    
    # WELLS information
    url="http://10.0.3.23:8787/wells/?format=json"
    wells_res=urllib.urlopen(url)
    wellsjsondata=json.loads(wells_res.read())
    
    # CROP information
    url="http://10.0.3.23:8787/crop/?format=json"
    crop_res=urllib.urlopen(url)
    cropjsondata=json.loads(crop_res.read())
    
    # FaRM information
    url="http://10.0.3.23:8787/publicplaces/?format=json"
    publicplaces_res=urllib.urlopen(url)
    publicplacesjsondata=json.loads(publicplaces_res.read())
    #RENDER the info to tdmp.html in dictionaries-
    return render(request, 'maps/tdmap.html', {'farmer':farmerjsondata,'farm':farmjsondata, 'house':housejsondata, 'farmpoints':farmpointsjsondata, 'wells':wellsjsondata,'publicplaces':publicplacesjsondata, 'members':membersjsondata, 'crop':cropjsondata})
    
    
    # DO THE SAME AS ABOVE TO SEND IT TO DUPLICATE tdmap1.html (WHICH IS A DUPLICATE USED FOR TESTING)
def mappoints1(request):
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
    
    return render(request, 'maps/c_1.html', {'farmer':farmerjsondata,'farm':farmjsondata, 'house':housejsondata, 'farmpoints':farmpointsjsondata, 'wells':wellsjsondata,'publicplaces':publicplacesjsondata, 'members':membersjsondata, 'crop':cropjsondata})
    

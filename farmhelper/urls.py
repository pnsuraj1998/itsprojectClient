"""farmhelper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from maps import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),                                                           #Access admin
    url(r'^allmaps/', include('maps.urls')),                                                   
    url(r'^allhouse/', views.housetable, name= 'house'),                                        #Access House table
    url(r'^allfarmer/',views.farmertable, name= 'farmer'),                                       #Access Farmer table
    url(r'^allfarm/',views.farmtable, name= 'farm'),                                             #Access Farm table
    url(r'^allfarmpoints/',views.farmpointstable, name= 'farmpoints'),                          #Access FarmCoordinates
    url(r'^allwells/',views.wellstable, name= 'wells'),                                         #Access Wells table
    url(r'^allpublicplaces/',views.publicplacestable, name= 'publicplaces'),                    #Access PublicPlaces table
    url(r'^allmembers/',views.memberstable, name= 'members'),                                   #Access Family members of Farmer
    url(r'^allcrop/',views.croptable, name= 'crop'),                                            #Access Cropping Details of Farm
    url(r'^maps/',views.mappoints,name='mappoints'),                                            #Access Map page(main page)
    url(r'^dupmaps/',views.mappoints1,name='mappoints1'),                                       #Access test map page
]

urlpatterns=format_suffix_patterns(urlpatterns)

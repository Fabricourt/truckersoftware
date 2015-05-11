from django.conf.urls import include, url
from django.contrib import admin
from FApp.views import * 

urlpatterns = [
    url(r'^accounts/login', login, name='login'),
    url(r'^validate/', validate),
    url(r'^accounts/logout', logout , name='logout'),
    url(r'accounts/invalid',invalid),
    url(r'^$',index),
    url(r'^orders/',orders),
    url(r'^shipper/',shipper),
    url(r'^reciever/',reciever),
    url(r'^billing/',billing),
    url(r'^paying/',paying),
    url(r'^equipment/',equipment),
    url(r'^carrier/',carrier),
    url(r'^shipper/',shipper),
    url(r'^driver/',add_driver),
    url(r'^truck/',add_truck),
    url(r'^trailer/',add_trailer),
    url(r'shipper_info/(?P<pid>\d+)/$', shipper_info),
    url(r'reciever_info/(?P<pid>\d+)/$', reciever_info),
    url(r'carrier_info/(?P<pid>\d+)/$', carrier_info),
    url(r'billing_info/(?P<pid>\d+)/$', billing_info),
    url(r'paying_info/(?P<pid>\d+)/$', paying_info),
    url(r'equipment_info/(?P<pid>\d+)/$', equipment_info),
    url(r'truck_info/(?P<pid>\d+)/$', equipment_info),
    url(r'trailer_info/(?P<pid>\d+)/$', equipment_info),
    url(r'get_details/(?P<pid>\d+)/$', get_details),
    url(r'update_status/(?P<pid>\d+)/$', update_status),
    url(r'^admin/', include(admin.site.urls)),
]

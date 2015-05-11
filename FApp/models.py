from django.db import models
from django.utils.timezone import now
import datetime
from django.contrib.auth.models import User

equipments=(
    ("22' Van","22' Van"),
    ("48' Reefer","48' Reefer"),
    ("53' Reefer","53' Reefer"),
    ("53' Van","53' Van"),
    ('Air freight','Air freight'),
    ('Airride/Logistical Van','Airride/Logistical Van'),
    ('Anydros Ammonia','Anydros Ammonia'),
    ('Animal Carrier', 'Animal Carrier'),
    ('Any Equipment','Any Equipment'),
    ('Auto Carrier','Auto Carrier'),
    ('B-Train/Superman','B-Train/Superman'),
    ('B-Train/Superman(Canada Only)','B-Train/Superman(Canada Only)'),
    ('Beam','Beam'),
    ('Belly Dump','Belly Dump'),
    ('Blanket Wrap Van','Blanket Wrap Van'),
    ('Boat Hauling Trailer', 'Boat Hauling Trailer'),
    ('Cargo Van(1 ton)','Cargo Van(1 ton)'),
    ('Cargo Van(1 ton capacity)','Cargo Van(1 ton capacity)'),
    ('Covestoga','Covestoga'),
    ('Container Trailer','Container Trailer'),
    ('Convertable Hopper','Convertable Hopper'),
    ('Conveyer Belt','Conveyer Belt'),
    ('Crane Truck','Crane Truck'),
    ('Curtain Sider','Curtain Sider'),
    ('Curtain Van','Curtain Van'),
    ('Double Drop','Double Drop'),
    ('Double Drop Extendables','Double Drop Extendables'),
    ('Drive Away','Drive Away'),
    ('Dump Trucks','Dump Trucks'),
    ('End dump','End dump'),
    ('Flat InterModal','Flat InterModal'),
    ('Flat or step Deck','Flat or step Deck'),
    ('Flat with tarps','Flat with tarps'),
    ('Flatbed','Flatbed'),
    ('Flatbed Air-Ride','Flatbed Air-Ride'),
    ('Flatbed AirRide','Flatbed AirRide'),
    ('Flatbed Blanket Wrapped','Flatbed Blanket Wrapped'),
    ('Flatbed InterModal','Flatbed InterModal'),
    ('Flatbed or Van','Flatbed or Van'),
    ('Flatbed overvented van','Flatbed overvented van'),
    )
Types=(
    ('25lbs Sacks','25lbs Stack'),
    ('40lbs Cartons','40lbs Cartons'),
    ('50lbs Sacks','50lbs Sacks'),
    ('Air Freight','Air Freight'),
    ('Barrels','Barrels'),
    ('Bushels','Bushels'),
    ('Cubic Yard','Cubic Yard'),
    ('CWT/100lbs','CWT/100lbs'),
    ('CWT/1lbs','CWT/1lbs'),
    ('CWT/1Ton','CWT/1Ton'),
    ('Delivery','Delivery'),
    ('Direct','Direct'),
    ('Drop','Drop'),
    ('Equip. Rental-Daily','Equip. Rental-Daily'),
    ('Equip. Rental-Monthly','Equip. Rental-Monthly'),
    ('Equip. Rental-Weekly','Equip. Rental-Weekly'),
    ('Feet','Feet'),
    ('FlatBed','FlatBed'),
    ('Full Truck Load','Full Truck Load'),
    ('Hot Shot','Hot Shot'),
    ('Hourly','Hourly'),
    ('Labour','Labour'),
    ('Line Haul','Line Haul'),
    ('LBS','LBS'),
    ('LTL','LTL'),
    ('Metric Ton','Metric Ton'),
    ('Ocean','Ocean'),
    ('Other','Other'),
    ('Pallets','Pallets'),
    ('Pickup','Pickup'),
    ('Piece','Piece'),
    ('Profit Share','Profit Share'),
    ('Rail','Rail'),
    ('RPM','RPM'),
    ('RPM(fsc)','RPM(fsc)'),
    ('Tons','Tons'),
    ('Truck Ordered Not Used','Truck Ordered Not Used'),
  )
status=(
    ('Dispatched', 'Dispatched'),
    ('Pending','Pending'),
    ('Complete','Complete'),
    ('Loaded','Loaded'),
    ('Unloaded','Unloaded'),
    ('Free','Free'),
    ('OnRoute','OnRoute'),
)
currency=(
    ('USD $','USD $'),
    ('CAD $','CAD $')
    )

dtype=(
     ('Single','Single'),
     ('Team','Team'),
    )
    
d_status=(
        ('Active','Active'),
        ('Inactive','Inactive'),
        ('Not Available','Not Available'),
        )
owner=(
        ('Company Truck','Company Truck'),
        ('Other','Other')
      )


class DriverModel(models.Model):
    name=models.CharField(max_length=100, unique=True)
    license_no=models.CharField(max_length=100, unique=True)
    license_expiry=models.DateField()
    driver_type=models.CharField(max_length=20,default='Single',choices=dtype)
    passport_no=models.CharField(max_length=100,default='')
    passport_expiry=models.DateTimeField(default='')
    finished_tasks=models.IntegerField(default=0)
    assigned_tasks=models.IntegerField(default=0)
    reputation=models.IntegerField(default=1)  
    status=models.CharField(max_length=50,choices=d_status)
    country=models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.name
    
class TrailerInfo(models.Model):
    trailer_no=models.CharField(max_length=100,default='',unique=True)
    trailer_type=models.CharField(max_length=100,default='',choices=equipments)
    description=models.CharField(max_length=100,default='')
    ownership=models.CharField(max_length=50,choices=owner)
    
    def __unicode__(self):
        return self.trailer_no
    
class Truck(models.Model):
    truck_no=models.CharField(unique=True,max_length=100)
    truck_type=models.CharField(unique=True,max_length=100,choices=equipments)
    license_plate=models.CharField(max_length=100, default='')
    plate_expiry=models.DateTimeField()
    inspection_expiry=models.DateTimeField()
    description=models.CharField(max_length=200,default='')
    status=models.CharField(max_length=20,choices=d_status)
    ownership=models.CharField(max_length=50,choices=owner)
    
    def __unicode__(self):
        return self.truck_no
    
class OrderModel(models.Model):
    order_no=models.CharField(max_length=100,unique=True)
    status=models.CharField(max_length=50, choices=status, default='Pending')
    creator=models.ForeignKey(User)
    shipper=models.CharField(max_length=200, default='')
    reciever=models.CharField(max_length=200, default='')
    charges=models.IntegerField()
    types=models.CharField(max_length=100, choices=Types)
    currency_type=models.CharField(max_length=10,choices=currency)
    edit_date=models.DateTimeField(auto_now=True)# exclude in forms
    truck=models.ForeignKey(Truck)
    trailer=models.ForeignKey(TrailerInfo)
    other_charges=models.IntegerField(default=0)
    total_charges=models.IntegerField(default=0)# exclude in forms
    
    def __unicode__(self):
        return self.order_no
    
class ShipperInfo(models.Model):
    for_order=models.ForeignKey(OrderModel, to_field='order_no')
    shipping_date=models.DateTimeField(default=now)
    shipper=models.CharField(max_length=100,default='',unique=True)
    address=models.CharField(max_length=200,default='')
    city=models.CharField(max_length=100,default='')
    state=models.CharField(max_length=100,default='')
    zip_code=models.IntegerField(default='')
    contact_name=models.CharField(max_length=100,default='')
    email=models.EmailField(default='')
    phone_no=models.IntegerField(default='')
    
    def __unicode__(self):
        return self.shipper
    
class RecieverInfo(models.Model):
    for_order=models.ForeignKey(OrderModel, to_field='order_no')
    delivery_date=models.DateTimeField()
    reciever=models.CharField(max_length=100,default='',unique=True)
    address=models.CharField(max_length=200,default='')
    city=models.CharField(max_length=100,default='')
    state=models.CharField(max_length=100,default='')
    zip_code=models.IntegerField(default='')
    contact_name=models.CharField(max_length=100,default='')
    email=models.EmailField(default='')
    phone_no=models.IntegerField(default='')
    
    def __unicode__(self):
        return self.reciever
    
class BillTo(models.Model):
    for_order=models.ForeignKey(OrderModel, to_field='order_no')
    bill_to=models.CharField(max_length=100,default='')
    address=models.CharField(max_length=100,default='')
    city=models.CharField(max_length=100,default='')
    state=models.CharField(max_length=100,default='')
    zipcode=models.IntegerField(default='')
    contact_name=models.CharField(max_length=100,default='')
    total_charges=models.IntegerField(default='')
    
    def __unicode__(self):
        return self.bill_to

class PayTo(models.Model):
    for_order=models.ForeignKey(OrderModel, to_field='order_no')
    pay_to=models.CharField(max_length=100,default='')
    address=models.CharField(max_length=100,default='')
    city=models.CharField(max_length=100,default='')
    state=models.CharField(max_length=100,default='')
    zipcode=models.IntegerField(default='')
    contact_name=models.CharField(max_length=100,default='')
    total_charges=models.IntegerField(default='')
    
    def __unicode__(self):
        return self.pay_to
    
class EquipmentInfo(models.Model):
    for_order=models.ForeignKey(OrderModel, to_field='order_no')
    dispatch_location=models.CharField(max_length=100,default='')
    driver_name=models.ForeignKey(DriverModel,to_field='license_no')
    driver_cell=models.CharField(default='',max_length=100)
    load_weight=models.IntegerField(default='')
    truck_no=models.ForeignKey(Truck, to_field='truck_no')
    trailer_no=models.ForeignKey(TrailerInfo,to_field='trailer_no')
    equipment_type=models.CharField(default='',max_length=200,choices=equipments)
    total_kms=models.IntegerField( default='')
    loaded_material=models.CharField(default='',max_length=200)
    
    def __unicode__(self):
        return self.loaded_material

class CarrierInfo(models.Model):
    for_order=models.ForeignKey(OrderModel, to_field='order_no')
    carrier=models.CharField(default='',max_length=100)
    address=models.CharField(default='',max_length=100)
    city=models.CharField(default='',max_length=100)
    state=models.CharField(default='',max_length=100)
    contact_name=models.CharField(default='',max_length=100)
    email=models.EmailField(default='')
    ph_no=models.IntegerField(default='')
    fax_no=models.IntegerField(default='')
    
    def __unicode__(self):
        return self.carrier




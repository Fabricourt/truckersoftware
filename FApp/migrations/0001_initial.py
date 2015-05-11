# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BillTo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bill_to', models.CharField(default=b'', max_length=100)),
                ('address', models.CharField(default=b'', max_length=100)),
                ('city', models.CharField(default=b'', max_length=100)),
                ('state', models.CharField(default=b'', max_length=100)),
                ('zipcode', models.IntegerField(default=b'')),
                ('contact_name', models.CharField(default=b'', max_length=100)),
                ('total_charges', models.IntegerField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='CarrierInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('carrier', models.CharField(default=b'', max_length=100)),
                ('address', models.CharField(default=b'', max_length=100)),
                ('city', models.CharField(default=b'', max_length=100)),
                ('state', models.CharField(default=b'', max_length=100)),
                ('contact_name', models.CharField(default=b'', max_length=100)),
                ('email', models.EmailField(default=b'', max_length=254)),
                ('ph_no', models.IntegerField(default=b'')),
                ('fax_no', models.IntegerField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='DriverModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('license_no', models.CharField(unique=True, max_length=100)),
                ('license_expiry', models.DateField()),
                ('driver_type', models.CharField(default=b'Single', max_length=20, choices=[(b'Single', b'Single'), (b'Team', b'Team')])),
                ('passport_no', models.CharField(default=b'', max_length=100)),
                ('passport_expiry', models.DateTimeField(default=b'')),
                ('finished_tasks', models.IntegerField(default=0)),
                ('assigned_tasks', models.IntegerField(default=0)),
                ('reputation', models.IntegerField(default=1)),
                ('status', models.CharField(max_length=50, choices=[(b'Active', b'Active'), (b'Inactive', b'Inactive'), (b'Not Available', b'Not Available')])),
                ('country', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='EquipmentInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dispatch_location', models.CharField(default=b'', max_length=100)),
                ('driver_cell', models.CharField(default=b'', max_length=100)),
                ('load_weight', models.IntegerField(default=b'')),
                ('equipment_type', models.CharField(default=b'', max_length=200, choices=[(b"22' Van", b"22' Van"), (b"48' Reefer", b"48' Reefer"), (b"53' Reefer", b"53' Reefer"), (b"53' Van", b"53' Van"), (b'Air freight', b'Air freight'), (b'Airride/Logistical Van', b'Airride/Logistical Van'), (b'Anydros Ammonia', b'Anydros Ammonia'), (b'Animal Carrier', b'Animal Carrier'), (b'Any Equipment', b'Any Equipment'), (b'Auto Carrier', b'Auto Carrier'), (b'B-Train/Superman', b'B-Train/Superman'), (b'B-Train/Superman(Canada Only)', b'B-Train/Superman(Canada Only)'), (b'Beam', b'Beam'), (b'Belly Dump', b'Belly Dump'), (b'Blanket Wrap Van', b'Blanket Wrap Van'), (b'Boat Hauling Trailer', b'Boat Hauling Trailer'), (b'Cargo Van(1 ton)', b'Cargo Van(1 ton)'), (b'Cargo Van(1 ton capacity)', b'Cargo Van(1 ton capacity)'), (b'Covestoga', b'Covestoga'), (b'Container Trailer', b'Container Trailer'), (b'Convertable Hopper', b'Convertable Hopper'), (b'Conveyer Belt', b'Conveyer Belt'), (b'Crane Truck', b'Crane Truck'), (b'Curtain Sider', b'Curtain Sider'), (b'Curtain Van', b'Curtain Van'), (b'Double Drop', b'Double Drop'), (b'Double Drop Extendables', b'Double Drop Extendables'), (b'Drive Away', b'Drive Away'), (b'Dump Trucks', b'Dump Trucks'), (b'End dump', b'End dump'), (b'Flat InterModal', b'Flat InterModal'), (b'Flat or step Deck', b'Flat or step Deck'), (b'Flat with tarps', b'Flat with tarps'), (b'Flatbed', b'Flatbed'), (b'Flatbed Air-Ride', b'Flatbed Air-Ride'), (b'Flatbed AirRide', b'Flatbed AirRide'), (b'Flatbed Blanket Wrapped', b'Flatbed Blanket Wrapped'), (b'Flatbed InterModal', b'Flatbed InterModal'), (b'Flatbed or Van', b'Flatbed or Van'), (b'Flatbed overvented van', b'Flatbed overvented van')])),
                ('total_kms', models.IntegerField(default=b'')),
                ('loaded_material', models.CharField(default=b'', max_length=200)),
                ('drive_name', models.ForeignKey(to='FApp.DriverModel', to_field=b'license_no')),
            ],
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_no', models.CharField(unique=True, max_length=100)),
                ('status', models.CharField(default=b'Pending', max_length=50, choices=[(b'Dispatched', b'Dispatched'), (b'Pending', b'Pending'), (b'Complete', b'Complete'), (b'Loaded', b'Loaded'), (b'Unloaded', b'Unloaded'), (b'Free', b'Free'), (b'OnRoute', b'OnRoute')])),
                ('shipper', models.CharField(default=b'', max_length=200)),
                ('reciever', models.CharField(default=b'', max_length=200)),
                ('charges', models.IntegerField()),
                ('types', models.CharField(max_length=100, choices=[(b'25lbs Sacks', b'25lbs Stack'), (b'40lbs Cartons', b'40lbs Cartons'), (b'50lbs Sacks', b'50lbs Sacks'), (b'Air Freight', b'Air Freight'), (b'Barrels', b'Barrels'), (b'Bushels', b'Bushels'), (b'Cubic Yard', b'Cubic Yard'), (b'CWT/100lbs', b'CWT/100lbs'), (b'CWT/1lbs', b'CWT/1lbs'), (b'CWT/1Ton', b'CWT/1Ton'), (b'Delivery', b'Delivery'), (b'Direct', b'Direct'), (b'Drop', b'Drop'), (b'Equip. Rental-Daily', b'Equip. Rental-Daily'), (b'Equip. Rental-Monthly', b'Equip. Rental-Monthly'), (b'Equip. Rental-Weekly', b'Equip. Rental-Weekly'), (b'Feet', b'Feet'), (b'FlatBed', b'FlatBed'), (b'Full Truck Load', b'Full Truck Load'), (b'Hot Shot', b'Hot Shot'), (b'Hourly', b'Hourly'), (b'Labour', b'Labour'), (b'Line Haul', b'Line Haul'), (b'LBS', b'LBS'), (b'LTL', b'LTL'), (b'Metric Ton', b'Metric Ton'), (b'Ocean', b'Ocean'), (b'Other', b'Other'), (b'Pallets', b'Pallets'), (b'Pickup', b'Pickup'), (b'Piece', b'Piece'), (b'Profit Share', b'Profit Share'), (b'Rail', b'Rail'), (b'RPM', b'RPM'), (b'RPM(fsc)', b'RPM(fsc)'), (b'Tons', b'Tons'), (b'Truck Ordered Not Used', b'Truck Ordered Not Used')])),
                ('currency_type', models.CharField(max_length=10, choices=[(b'USD $', b'USD $'), (b'CAD $', b'CAD $')])),
                ('edit_date', models.DateTimeField(auto_now=True)),
                ('other_charges', models.IntegerField(default=0)),
                ('total_charges', models.IntegerField(default=0)),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PayTo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pay_to', models.CharField(default=b'', max_length=100)),
                ('address', models.CharField(default=b'', max_length=100)),
                ('city', models.CharField(default=b'', max_length=100)),
                ('state', models.CharField(default=b'', max_length=100)),
                ('zipcode', models.IntegerField(default=b'')),
                ('contact_name', models.CharField(default=b'', max_length=100)),
                ('total_charges', models.IntegerField(default=b'')),
                ('for_order', models.ForeignKey(to='FApp.OrderModel', to_field=b'order_no')),
            ],
        ),
        migrations.CreateModel(
            name='RecieverInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('delivery_date', models.DateTimeField()),
                ('reciever', models.CharField(default=b'', unique=True, max_length=100)),
                ('address', models.CharField(default=b'', max_length=200)),
                ('city', models.CharField(default=b'', max_length=100)),
                ('state', models.CharField(default=b'', max_length=100)),
                ('zip_code', models.IntegerField(default=b'')),
                ('contact_name', models.CharField(default=b'', max_length=100)),
                ('email', models.EmailField(default=b'', max_length=254)),
                ('phone_no', models.IntegerField(default=b'')),
                ('for_order', models.ForeignKey(to='FApp.OrderModel', to_field=b'order_no')),
            ],
        ),
        migrations.CreateModel(
            name='ShipperInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('shipping_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('shipper', models.CharField(default=b'', unique=True, max_length=100)),
                ('address', models.CharField(default=b'', max_length=200)),
                ('city', models.CharField(default=b'', max_length=100)),
                ('state', models.CharField(default=b'', max_length=100)),
                ('zip_code', models.IntegerField(default=b'')),
                ('contact_name', models.CharField(default=b'', max_length=100)),
                ('email', models.EmailField(default=b'', max_length=254)),
                ('phone_no', models.IntegerField(default=b'')),
                ('for_order', models.ForeignKey(to='FApp.OrderModel', to_field=b'order_no')),
            ],
        ),
        migrations.CreateModel(
            name='TrailerInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('trailer_no', models.CharField(default=b'', unique=True, max_length=100)),
                ('trailer_type', models.CharField(default=b'', max_length=100, choices=[(b"22' Van", b"22' Van"), (b"48' Reefer", b"48' Reefer"), (b"53' Reefer", b"53' Reefer"), (b"53' Van", b"53' Van"), (b'Air freight', b'Air freight'), (b'Airride/Logistical Van', b'Airride/Logistical Van'), (b'Anydros Ammonia', b'Anydros Ammonia'), (b'Animal Carrier', b'Animal Carrier'), (b'Any Equipment', b'Any Equipment'), (b'Auto Carrier', b'Auto Carrier'), (b'B-Train/Superman', b'B-Train/Superman'), (b'B-Train/Superman(Canada Only)', b'B-Train/Superman(Canada Only)'), (b'Beam', b'Beam'), (b'Belly Dump', b'Belly Dump'), (b'Blanket Wrap Van', b'Blanket Wrap Van'), (b'Boat Hauling Trailer', b'Boat Hauling Trailer'), (b'Cargo Van(1 ton)', b'Cargo Van(1 ton)'), (b'Cargo Van(1 ton capacity)', b'Cargo Van(1 ton capacity)'), (b'Covestoga', b'Covestoga'), (b'Container Trailer', b'Container Trailer'), (b'Convertable Hopper', b'Convertable Hopper'), (b'Conveyer Belt', b'Conveyer Belt'), (b'Crane Truck', b'Crane Truck'), (b'Curtain Sider', b'Curtain Sider'), (b'Curtain Van', b'Curtain Van'), (b'Double Drop', b'Double Drop'), (b'Double Drop Extendables', b'Double Drop Extendables'), (b'Drive Away', b'Drive Away'), (b'Dump Trucks', b'Dump Trucks'), (b'End dump', b'End dump'), (b'Flat InterModal', b'Flat InterModal'), (b'Flat or step Deck', b'Flat or step Deck'), (b'Flat with tarps', b'Flat with tarps'), (b'Flatbed', b'Flatbed'), (b'Flatbed Air-Ride', b'Flatbed Air-Ride'), (b'Flatbed AirRide', b'Flatbed AirRide'), (b'Flatbed Blanket Wrapped', b'Flatbed Blanket Wrapped'), (b'Flatbed InterModal', b'Flatbed InterModal'), (b'Flatbed or Van', b'Flatbed or Van'), (b'Flatbed overvented van', b'Flatbed overvented van')])),
                ('description', models.CharField(default=b'', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('truck_no', models.CharField(unique=True, max_length=100)),
                ('license_plate', models.CharField(default=b'', max_length=100)),
                ('plate_expiry', models.DateTimeField()),
                ('inspection_expiry', models.DateTimeField()),
                ('description', models.CharField(default=b'', max_length=200)),
                ('status', models.CharField(max_length=20, choices=[(b'Active', b'Active'), (b'Inactive', b'Inactive'), (b'Not Available', b'Not Available')])),
                ('ownership', models.CharField(max_length=50, choices=[(b'Company Truck', b'Company Truck'), (b'Other', b'Other')])),
            ],
        ),
        migrations.CreateModel(
            name='TruckType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100, choices=[(b"22' Van", b"22' Van"), (b"48' Reefer", b"48' Reefer"), (b"53' Reefer", b"53' Reefer"), (b"53' Van", b"53' Van"), (b'Air freight', b'Air freight'), (b'Airride/Logistical Van', b'Airride/Logistical Van'), (b'Anydros Ammonia', b'Anydros Ammonia'), (b'Animal Carrier', b'Animal Carrier'), (b'Any Equipment', b'Any Equipment'), (b'Auto Carrier', b'Auto Carrier'), (b'B-Train/Superman', b'B-Train/Superman'), (b'B-Train/Superman(Canada Only)', b'B-Train/Superman(Canada Only)'), (b'Beam', b'Beam'), (b'Belly Dump', b'Belly Dump'), (b'Blanket Wrap Van', b'Blanket Wrap Van'), (b'Boat Hauling Trailer', b'Boat Hauling Trailer'), (b'Cargo Van(1 ton)', b'Cargo Van(1 ton)'), (b'Cargo Van(1 ton capacity)', b'Cargo Van(1 ton capacity)'), (b'Covestoga', b'Covestoga'), (b'Container Trailer', b'Container Trailer'), (b'Convertable Hopper', b'Convertable Hopper'), (b'Conveyer Belt', b'Conveyer Belt'), (b'Crane Truck', b'Crane Truck'), (b'Curtain Sider', b'Curtain Sider'), (b'Curtain Van', b'Curtain Van'), (b'Double Drop', b'Double Drop'), (b'Double Drop Extendables', b'Double Drop Extendables'), (b'Drive Away', b'Drive Away'), (b'Dump Trucks', b'Dump Trucks'), (b'End dump', b'End dump'), (b'Flat InterModal', b'Flat InterModal'), (b'Flat or step Deck', b'Flat or step Deck'), (b'Flat with tarps', b'Flat with tarps'), (b'Flatbed', b'Flatbed'), (b'Flatbed Air-Ride', b'Flatbed Air-Ride'), (b'Flatbed AirRide', b'Flatbed AirRide'), (b'Flatbed Blanket Wrapped', b'Flatbed Blanket Wrapped'), (b'Flatbed InterModal', b'Flatbed InterModal'), (b'Flatbed or Van', b'Flatbed or Van'), (b'Flatbed overvented van', b'Flatbed overvented van')])),
            ],
        ),
        migrations.AddField(
            model_name='truck',
            name='truck_type',
            field=models.ForeignKey(to='FApp.TruckType'),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='trailer',
            field=models.ForeignKey(to='FApp.TrailerInfo'),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='truck',
            field=models.ForeignKey(to='FApp.Truck'),
        ),
        migrations.AddField(
            model_name='equipmentinfo',
            name='for_order',
            field=models.ForeignKey(to='FApp.OrderModel', to_field=b'order_no'),
        ),
        migrations.AddField(
            model_name='equipmentinfo',
            name='trailer_no',
            field=models.ForeignKey(to='FApp.TrailerInfo', to_field=b'trailer_no'),
        ),
        migrations.AddField(
            model_name='equipmentinfo',
            name='truck_no',
            field=models.ForeignKey(to='FApp.Truck', to_field=b'truck_no'),
        ),
        migrations.AddField(
            model_name='carrierinfo',
            name='for_order',
            field=models.ForeignKey(to='FApp.OrderModel', to_field=b'order_no'),
        ),
        migrations.AddField(
            model_name='billto',
            name='for_order',
            field=models.ForeignKey(to='FApp.OrderModel', to_field=b'order_no'),
        ),
    ]

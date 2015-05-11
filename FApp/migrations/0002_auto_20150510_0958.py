# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='truck',
            name='truck_type',
            field=models.CharField(unique=True, max_length=100, choices=[(b"22' Van", b"22' Van"), (b"48' Reefer", b"48' Reefer"), (b"53' Reefer", b"53' Reefer"), (b"53' Van", b"53' Van"), (b'Air freight', b'Air freight'), (b'Airride/Logistical Van', b'Airride/Logistical Van'), (b'Anydros Ammonia', b'Anydros Ammonia'), (b'Animal Carrier', b'Animal Carrier'), (b'Any Equipment', b'Any Equipment'), (b'Auto Carrier', b'Auto Carrier'), (b'B-Train/Superman', b'B-Train/Superman'), (b'B-Train/Superman(Canada Only)', b'B-Train/Superman(Canada Only)'), (b'Beam', b'Beam'), (b'Belly Dump', b'Belly Dump'), (b'Blanket Wrap Van', b'Blanket Wrap Van'), (b'Boat Hauling Trailer', b'Boat Hauling Trailer'), (b'Cargo Van(1 ton)', b'Cargo Van(1 ton)'), (b'Cargo Van(1 ton capacity)', b'Cargo Van(1 ton capacity)'), (b'Covestoga', b'Covestoga'), (b'Container Trailer', b'Container Trailer'), (b'Convertable Hopper', b'Convertable Hopper'), (b'Conveyer Belt', b'Conveyer Belt'), (b'Crane Truck', b'Crane Truck'), (b'Curtain Sider', b'Curtain Sider'), (b'Curtain Van', b'Curtain Van'), (b'Double Drop', b'Double Drop'), (b'Double Drop Extendables', b'Double Drop Extendables'), (b'Drive Away', b'Drive Away'), (b'Dump Trucks', b'Dump Trucks'), (b'End dump', b'End dump'), (b'Flat InterModal', b'Flat InterModal'), (b'Flat or step Deck', b'Flat or step Deck'), (b'Flat with tarps', b'Flat with tarps'), (b'Flatbed', b'Flatbed'), (b'Flatbed Air-Ride', b'Flatbed Air-Ride'), (b'Flatbed AirRide', b'Flatbed AirRide'), (b'Flatbed Blanket Wrapped', b'Flatbed Blanket Wrapped'), (b'Flatbed InterModal', b'Flatbed InterModal'), (b'Flatbed or Van', b'Flatbed or Van'), (b'Flatbed overvented van', b'Flatbed overvented van')]),
        ),
        migrations.DeleteModel(
            name='TruckType',
        ),
    ]

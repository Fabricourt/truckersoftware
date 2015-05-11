from __future__ import division # to yeild the decimal point values in Python 2.x
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import auth
from django.core.context_processors import csrf
from FApp.views import *
from FApp.models import *
from FApp.forms import *
from django.utils import timezone
from django.template import *
from datetime import datetime
from dateutil.parser import parse # to parse the unicode date



# --------------------------login views start------------------------------------- #
def login(request):
    c={}
    c.update(csrf(request))
    return render_to_response('login.html',c)

@login_required   
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/accounts/login/')

def invalid(request):
    return render_to_response('invalid.html')

# --------------------------login views end------------------------------------- #

# ------------------------------ App Views ----------------------------------------#
@login_required
def index(request):
    c={}
    c['data']=OrderModel.objects.order_by('edit_date').reverse()[:10]
    c['driver']=DriverModel.objects.order_by('reputation').reverse()[:10]
    return render_to_response('index.html',c)

@login_required
def shipper_info(request,pid):
    c={}
    c['data']=OrderModel.objects.order_by('edit_date').reverse()[:20]
    c['driver']=DriverModel.objects.order_by('reputation').reverse()
    c['info']=ShipperInfo.objects.get(for_order_id=pid)
    c['title']='Shipping'
    return render_to_response('index.html',c)

def reciever_info(request,pid):
    c={}
    c['data']=OrderModel.objects.order_by('edit_date').reverse()[:20]
    c['driver']=DriverModel.objects.order_by('reputation').reverse()
    c['info']=RecieverInfo.objects.get(for_order_id=pid)
    c['title']='Recieving'
    return render_to_response('index.html',c)

def equipment_info(request, pid):
    c={}
    c['data']=OrderModel.objects.order_by('edit_date').reverse()[:20]
    c['driver']=DriverModel.objects.order_by('reputation').reverse()
    c['details']=EquipmentInfo.objects.get(for_order_id=pid)
    c['title']='Equipment'
    return render_to_response('index.html',c)

def billing_info(request,pid):
    c={}
    c['data']=OrderModel.objects.order_by('edit_date').reverse()[:20]
    c['driver']=DriverModel.objects.order_by('reputation').reverse()
    c['bill_pay']=BillTo.objects.get(for_order_id=pid)
    c['title']='Bill'
    return render_to_response('index.html',c)

def paying_info(request,pid):
    c={}
    c['data']=OrderModel.objects.order_by('edit_date').reverse()[:20]
    c['driver']=DriverModel.objects.order_by('reputation').reverse()
    c['bill_pay']=PayTo.objects.get(for_order_id=pid)
    c['title']='Pay'
    return render_to_response('index.html',c)

def carrier_info(request,pid):
    c={}
    c['data']=OrderModel.objects.order_by('edit_date').reverse()[:20]
    c['driver']=DriverModel.objects.order_by('reputation').reverse()
    c['carrier']=CarrierInfo.objects.get(for_order_id=pid)
    c['title']='Carrier'
    return render_to_response('index.html',c)

def validate(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    user= auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/')
    else :
        return HttpResponseRedirect('/accounts/invalid/')
@login_required
def orders(request):
    if request.POST:
        c=request.POST.get('charges')
        b=request.POST.get('other_charges')
        order=request.POST.get('order_no')
        form= OrderForm(request.POST)
        if form.is_valid():
            form.save()
            a=OrderModel.objects.get(order_no=order)
            a.total_charges=int(c)+int(b)
            a.save()
            c={}
            c.update(csrf(request))
            c['path']='/shipper/'
            c['form']=ShipperForm
            c['title']= "SHIPPING INFO"
            return render_to_response('forms.html',c,context_instance=RequestContext(request))
    else:
        form=OrderForm
    a={}
    a.update(csrf(request))
    a['path']='/orders/'
    a['form']=form
    a['title']= "ORDER INFO"
    a['button']="PROCEED TO SHIPPING DETAILS"
    return render_to_response('forms.html',a,context_instance=RequestContext(request))


@login_required
def shipper(request):
    if request.POST:
        form= ShipperForm(request.POST)
        if form.is_valid():
            form.save()
            c={}
            c.update(csrf(request))
            c['path']='/reciever/'
            c['form']=RecieverForm
            c['title']= "RECIEVING INFO"
            c['button']="PROCEED TO BILL TO DETAILS"
            return render_to_response('forms.html',c,context_instance=RequestContext(request))
    else:
        form=ShipperForm
    a={}
    a.update(csrf(request))
    a['path']='/shipper/'
    a['form']=form
    a['title']= "SHIPPING INFO"
    a['button']="PROCEED TO RECIEVERS DETAILS"
    return render_to_response('forms.html',a,context_instance=RequestContext(request))


@login_required
def reciever(request):
    if request.POST:
        form= RecieverForm(request.POST)
        if form.is_valid():
            form.save()
            c={}
            c.update(csrf(request))
            c['path']='/billing/'
            c['form']=BillingForm
            c['title']= "BILL TO INFO"
            c['button']="PROCEED TO PAY TO DETAILS"
            return render_to_response('forms.html',c,context_instance=RequestContext(request))
    else:
        form=RecieverForm
    a={}
    a.update(csrf(request))
    a['path']='/reciever/'
    a['form']=form
    a['title']= "RECIEVING INFO"
    a['button']="PROCEED TO BILL TO DETAILS"
    return render_to_response('forms.html',a,context_instance=RequestContext(request))

@login_required
def billing(request):
    if request.POST:
        form= BillingForm(request.POST)
        if form.is_valid():
            form.save()
            c={}
            c.update(csrf(request))
            c['path']='/paying/'
            c['form']=PayingForm
            c['title']= "PAY TO INFO"
            c['button']="PROCEED TO EQUIPMENT DETAILS"
            return render_to_response('forms.html',c,context_instance=RequestContext(request))
    else:
        form=BillingForm
    a={}
    a.update(csrf(request))
    a['path']='/billing/'
    a['form']=form
    a['title']= "BILL TO INFO"
    a['button']="PROCEED TO PAY TO DETAILS"
    return render_to_response('forms.html',a,context_instance=RequestContext(request))

@login_required
def paying(request):
    if request.POST:
        form= PayingForm(request.POST)
        if form.is_valid():
            form.save()
            c={}
            c.update(csrf(request))
            c['path']='/equipment/'
            c['form']=EquipmentForm
            c['title']= "EQUIPMENT INFO"
            c['button']="PROCEED TO CARRIER DETAILS"
            return render_to_response('forms.html',c,context_instance=RequestContext(request))
    else:
        form=PayingForm
    a={}
    a.update(csrf(request))
    a['path']='/paying/'
    a['form']=form
    a['title']= "PAY TO INFO"
    a['button']="PROCEED TO PAY TO DETAILS"
    return render_to_response('forms.html',a,context_instance=RequestContext(request))

@login_required
def equipment(request):
    if request.POST:
        form= EquipmentForm(request.POST)
        dl=request.POST.get('driver_name')
        if form.is_valid():
            form.save()
            b=DriverModel.objects.get(license_no=dl)
            task=b.assigned_tasks
            task+=1
            b.assigned_tasks=task
            b.reputation=reputation(b.finished_tasks,b.assigned_tasks)
            b.save()
            c={}
            c.update(csrf(request))
            c['path']='/carrier/'
            c['form']=CarrierForm
            c['title']= "CARRIER INFO"
            return render_to_response('forms.html',c,context_instance=RequestContext(request))
    else:
        form=EquipmentForm
    a={}
    a.update(csrf(request))
    a['path']='/equipment/'
    a['form']=form
    a['title']= "EQUIPMENT INFO "
    a['button']="PROCEED TO PAY TO DETAILS"
    return render_to_response('forms.html',a,context_instance=RequestContext(request))

@login_required
def carrier(request):
    if request.POST:
        form= CarrierForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form=CarrierForm
    a={}
    a.update(csrf(request))
    a['path']='/'
    a['form']=form
    a['title']= "CARRIER INFO"
    a['button']="SUBMIT DETAILS"
    return render_to_response('forms.html',a,context_instance=RequestContext(request))


@login_required
def add_driver(request):
    if request.POST:
        form= DriverForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/#profile')
    else:
        form=DriverForm()
    args={}
    args.update(csrf(request))
    args['form']=form
    args['path']='/driver/'
    return render_to_response('add.html',args)

@login_required
def add_truck(request):
    if request.POST:
        form= TruckForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form=TruckForm()
    args={}
    args.update(csrf(request))
    args['form']=form
    args['path']='/truck/'
    return render_to_response('add.html',args)

@login_required
def add_trailer(request):
    if request.POST:
        form= TrailerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form=TrailerForm()
    args={}
    args.update(csrf(request))
    args['form']=form
    args['path']='/trailer/'
    return render_to_response('add.html',args)

def reputation(complete, assigned):
    rep=float((complete/assigned)*5)
    rep=round(rep)
    if rep==0:
        return 1
    else :
        return rep
    
@login_required
def update_status(request, pid):
    a=OrderModel.objects.get(order_no=pid)
    if request.POST:
        status=request.POST.get('update_status')
        a.status=status
        e=EquipmentInfo.objects.get(for_order=pid)
        dl=e.driver_name
        if 'Complete' in a.status:
            d=DriverModel.objects.get(license_no=dl)
            if d is not None:
                x=d.finished_tasks
                x+=1
                d.finished_tasks=x
                d.reputation=reputation(d.finished_tasks, d.assigned_tasks)
                d.save()
        a.save()
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
    
def get_details(request, pid):
    c={}
    c.update(csrf(request))
    try:
        c['order']=OrderModel.objects.get(order_no=pid)
    except :
        c['order']='No Info Available'
    try:
        c['shipper']=ShipperInfo.objects.get(for_order=pid)
    except :
        c['shipper']='No Info Available'
    try:
        c['reciever']=RecieverInfo.objects.get(for_order=pid)
    except :
        c['reciever']='No Info Available'
    try:
        c['bill']=BillTo.objects.get(for_order=pid)
    except :
        c['bill']='No Info Available'
    try:
        c['pay']=PayTo.objects.get(for_order=pid)
    except :
        c['pay']='No Info Available'
    try:
        c['equipment']=EquipmentInfo.objects.get(for_order=pid)
    except :
        c['equipment']='No Info Available'
    try:
        c['carrier']=CarrierInfo.objects.get(for_order=pid)
    except :
        c['carrier']='No Info Available'
    
    
    return render_to_response('details.html',c)


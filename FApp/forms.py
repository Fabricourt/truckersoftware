from django import forms
from models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, ButtonHolder
from crispy_forms.bootstrap import FormActions



class OrderForm(forms.ModelForm):
    
    helper=FormHelper()
    helper.layout = Layout(
        Div(
        Div(
            Div('order_no', css_class='col-md-4'),
            Div('shipper',css_class='col-md-4'),
            Div('reciever',css_class='col-md-4'),
            css_class='row-fluid'),
        
       Div(
            Div('status', css_class='col-md-5'),
            Div('creator',css_class='col-md-4'),
            Div('charges',css_class='col-md-3'),
            
            
        css_class='row-fluid'),
           
       Div(
            Div('truck',css_class='col-md-6'),
            Div('trailer',css_class='col-md-6'),
            css_class='row-fluid'
            ),
            
        Div(
            Div('types',css_class='col-md-4'),
            Div('currency_type',css_class='col-md-4'),
            Div('other_charges',css_class='col-md-4'),
            css_class='row-fluid'
            ),
        Div(
            Div('origin',css_class='col-md-4'),
            Div('destination',css_class='col-md-4'),
            Div('total_km',css_class='col-md-4'),
            css_class='row-fluid'
            ),
        ButtonHolder(
                Submit('submit', 'PROCEED TO SHIPPER INFO', css_class='button white btn-lg')
            ),
        
        css_class="container-fluid"),
           
        )
    
    
    class Meta:
        model= OrderModel
        exclude=['edit_date','total_charges']
        
        
class ShipperForm(forms.ModelForm):
    helper=FormHelper()
    helper.layout = Layout(
        Div(
        Div(
            Div('for_order', css_class='col-md-6'),
            Div('shipping_date',css_class='col-md-6'),
            css_class='row-fluid'),
        
       Div(
            Div('shipper', css_class='col-md-12'),
        css_class='row-fluid'),
           
       Div(
            Div('address',css_class='col-md-3'),
            Div('city',css_class='col-md-3'),
            Div('state',css_class='col-md-3'),
            Div('zip_code',css_class='col-md-3'),
            css_class='row-fluid'
            ),
            
        Div(
            Div('contact_name',css_class='col-md-4'),
            Div('email',css_class='col-md-4'),
            Div('phone_no',css_class='col-md-4'),
            css_class='row-fluid'
            ),
        ButtonHolder(
                Submit('submit', 'PROCEED TO RECIEVER INFO', css_class='button white btn-lg')
            ),
            )
        )
    class Meta:
        model= ShipperInfo
        exclude=[]
        
    def __init__(self , *args, **kwargs):
        super(ShipperForm, self).__init__(*args, **kwargs)
        self.fields['shipping_date'].widget.attrs.update({'id':'datepicker'})

        
        
class RecieverForm(forms.ModelForm):
    helper=FormHelper()
    helper.layout = Layout(
        Div(
        Div(
            Div('for_order', css_class='col-md-6'),
            Div('delivery_date',css_class='col-md-6'),
            css_class='row-fluid'),
        
       Div(
            Div('reciever', css_class='col-md-12'),
        css_class='row-fluid'),
           
       Div(
            Div('address',css_class='col-md-3'),
            Div('city',css_class='col-md-3'),
            Div('state',css_class='col-md-3'),
            Div('zip_code',css_class='col-md-3'),
            css_class='row-fluid'
            ),
            
        Div(
            Div('contact_name',css_class='col-md-4'),
            Div('email',css_class='col-md-4'),
            Div('phone_no',css_class='col-md-4'),
            css_class='row-fluid'
            ),
        ButtonHolder(
                Submit('submit', 'PROCEED TO BILLING INFO', css_class='button white btn-lg')
            ),
                )
            )
    class Meta:
        model= RecieverInfo
        exclude=[]
        
    def __init__(self , *args, **kwargs):
        super(RecieverForm, self).__init__(*args, **kwargs)
        self.fields['delivery_date'].widget.attrs.update({'id':'datepicker'})
                    
class BillingForm(forms.ModelForm):
    helper=FormHelper()
    helper.layout = Layout(
        Div(
        Div(
            Div('for_order', css_class='col-md-6'),
            Div('bill_to',css_class='col-md-6'),
            css_class='row-fluid'),
        
       Div(
            Div('address', css_class='col-md-12'),
        css_class='row-fluid'),
           
       Div(
            Div('city',css_class='col-md-4'),
            Div('state',css_class='col-md-4'),
            Div('zipcode',css_class='col-md-4'),
            css_class='row-fluid'
            ),
            
        Div(
            Div('contact_name',css_class='col-md-4 col-md-offset-2'),
            Div('total_charges',css_class='col-md-4'),
            css_class='row-fluid'
            ),
        ButtonHolder(
                Submit('submit', 'PROCEED TO PAYING INFO', css_class='button white btn-lg')
            ),
                    )
                )
    class Meta:
        model= BillTo
        exclude=[]
        
class PayingForm(forms.ModelForm):
    helper=FormHelper()
    helper.layout = Layout(
        Div(
        Div(
            Div('for_order', css_class='col-md-6'),
            Div('bill_to',css_class='col-md-6'),
            css_class='row-fluid'),
        
       Div(
            Div('address', css_class='col-md-12'),
        css_class='row-fluid'),
           
       Div(
            Div('city',css_class='col-md-4'),
            Div('state',css_class='col-md-4'),
            Div('zipcode',css_class='col-md-4'),
            css_class='row-fluid'
            ),
            
        Div(
            Div('contact_name',css_class='col-md-4 col-md-offset-2'),
            Div('total_charges',css_class='col-md-4'),
            css_class='row-fluid'
            ),
        css_class='container-fluid'),
        ButtonHolder(
                Submit('submit', 'PROCEED TO EQUIPMENT INFO', css_class='button white btn-lg')
            ),
                )
    
    class Meta:
        model= PayTo
        exclude=[]
        
class EquipmentForm(forms.ModelForm):
    helper=FormHelper()
    helper.layout = Layout(
        Div(
        Div(
            Div('for_order', css_class='col-md-4'),
            Div('dispatch_location',css_class='col-md-4'),
            Div('driver_name',css_class='col-md-4'),
            
            css_class='row-fluid'),
        
       Div(
            Div('driver_cell', css_class='col-md-4'),
            Div('load_weight', css_class='col-md-4'),
            Div('total_kms', css_class='col-md-4'),
        css_class='row-fluid'),
           
       Div(
            Div('truck_no',css_class='col-md-4'),
            Div('trailer_no',css_class='col-md-4'),
            Div('equipment_type',css_class='col-md-4'),
            css_class='row-fluid'
            ),
            
        Div(
            Div('loaded_material',css_class='col-md-12'),
            css_class='row-fluid'
            ),
                   css_class='container-fluid' ),
        ButtonHolder(
                Submit('submit', 'PROCEED TO CARRIER INFO', css_class='button white btn-lg')
            ),
                )
    
    class Meta:
        model= EquipmentInfo
        exclude=[]
        
class CarrierForm(forms.ModelForm):
    helper=FormHelper()
    helper.layout = Layout(
        Div(
        Div(
            Div('for_order', css_class='col-md-4'),
            Div('carrier',css_class='col-md-4'),
            Div('contact_name',css_class='col-md-4'),
            css_class='row-fluid'),
        
       Div(
            Div('address', css_class='col-md-12'),
        css_class='row-fluid'),
           
       Div(
            Div('city',css_class='col-md-6'),
            Div('state',css_class='col-md-6'),
            css_class='row-fluid'
            ),
            
        Div(
            Div('ph_no',css_class='col-md-4 col-md-offset-2'),
            Div('fax_no',css_class='col-md-4'),
            css_class='row-fluid'
            ),
        ButtonHolder(
                Submit('submit', 'SUBMIT DETAILS', css_class='button white btn-lg')
            ),
                    )
                )
    class Meta:
        model= CarrierInfo
        exclude=[]
        
class DriverForm(forms.ModelForm):
    
    class Meta:
        model= DriverModel
        exclude=[]
        
    def __init__(self , *args, **kwargs):
        super(DriverForm, self).__init__(*args, **kwargs)
        self.fields['license_expiry'].widget.attrs.update({'id':'datepicker'})
        self.fields['passport_expiry'].widget.attrs.update({'id':'datepicker1'})
class TruckForm(forms.ModelForm):
    
    class Meta:
        model= Truck
        exclude=[]
        
class TrailerForm(forms.ModelForm):
    
    class Meta:
        model= TrailerInfo
        exclude=[]

        

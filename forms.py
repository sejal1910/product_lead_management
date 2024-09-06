from django import forms
from .models import Product, Lead

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['name', 'email', 'phone_number', 'interested_product']

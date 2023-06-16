from django import forms
from shop.models import OrderItem, Order

class AddQuantityForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['quantity']

class CheckForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['comments', 'phonenumber']

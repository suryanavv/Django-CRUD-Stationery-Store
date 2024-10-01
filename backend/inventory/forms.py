from django import forms
from .models import StationeryItem

class StationeryItemForm(forms.ModelForm):
    class Meta:
        model = StationeryItem
        fields = ['name', 'description', 'price', 'stock']

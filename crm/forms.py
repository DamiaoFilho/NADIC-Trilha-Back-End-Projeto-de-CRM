from django import forms
from .models import *

class sellForms(forms.Form):
    product = forms.ModelChoiceField(Stock.objects.all())
    quantity = forms.IntegerField()

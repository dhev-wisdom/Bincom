from django import forms
from .models import PollingUnit

class PollingUnitResultForm(forms.Form):
    polling_unit = forms.ModelChoiceField(queryset=PollingUnit.objects.all())
    party_results = forms.CharField(widget=forms.Textarea)

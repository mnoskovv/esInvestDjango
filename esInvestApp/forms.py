from django import forms

from .models import Deal

class DealForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = ['name','term', 'percent', 'summary']
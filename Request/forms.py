from .models import requests
from django import forms


class RequestForm(forms.ModelForm):
    username = forms.CharField(max_length=50, required=False, help_text='Enter your name.')
    location = forms.CharField(max_length=50, required=False, help_text='Enter the description of the location briefly.')
    request = forms.CharField(max_length=50, required=False, help_text='Enter the description of the problem briefly.')
    phonenumber = forms.IntegerField(required=False, help_text='Enter appropriate phone number.')

    class Meta:
        model = requests
        fields = ('username', 'location', 'request', 'phonenumber', )
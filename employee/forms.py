from django import forms

class ProfileForm(forms.Form):
    imei = forms.CharField(min_length=15,required=True)
    mac = forms.CharField(min_length=14,required=True)

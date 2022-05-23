from django import forms

class PatientSigninForm(forms.Form):
    userid = forms.CharField(label="Your Userid",max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
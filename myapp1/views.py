from django.shortcuts import render
from myapp1.forms import PatientSigninForm

# Create your views here.
def Signin(request):
    patient = PatientSigninForm()
    return render(request,'signin.html',{"patientform":patient})
from django.shortcuts import render
from django.views import View
from .forms import *
from django.contrib import messages

# Create your views here.
class SignUpView(View) :
    def get(self,request):
        fm = SignUpForm()
        return render(request, 'signUp.html', {'form':fm})
    def post(self,request):
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account created successfully !!')
            fm.save()    
        return render(request, 'signUp.html', {'form':fm})
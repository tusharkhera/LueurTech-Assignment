from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':''}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':''}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':''}))
    class Meta :
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']
        labels = {'email': 'Email', 'first_name':'First Name', 'last_name':'Last Name'}
        widgets = {'username': forms.TextInput(attrs={'class':''})}
from django import forms
from django.core import validators
from django.contrib.auth.models import User
import re


class StudentForm(forms.ModelForm):
    
    def clean_username(self):
        username = self.cleaned_data["username"]
        if len(username)<4:
            raise forms.ValidationError('Username must be at least 4 characters long')
        if not re.match(r'^[a-zA-Z]+$',username ):
            raise forms.ValidationError( 'username must contain only alphabetic characters.')
        return username
    
    def clean_password(self):
        password=self.cleaned_data['password']
        if len(password)<5:
            raise forms.ValidationError('password must be atleast 5 length long')
        return password
        
        
    phone_number=forms.CharField()
 
    class Meta:
        model=User
        fields=('username','email','password','phone_number')

    
from typing import Any
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms

class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username','first_name','last_name','email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control', 'placeholder':'Enter your username'})
        self.fields['first_name'].widget.attrs.update({'class':'form-control', 'placeholder':'Enter your first name'})
        self.fields['last_name'].widget.attrs.update({'class':'form-control', 'placeholder':'Enter your last name'})
        self.fields['email'].widget.attrs.update({'class':'form-control', 'placeholder':'Enter your email'})
        self.fields['password1'].widget.attrs.update({'class':'form-control', 'placeholder':'Create a password'})
        self.fields['password2'].widget.attrs.update({'class':'form-control', 'placeholder':'Confirm Password'})

    
class UpdateForm(UserChangeForm):
    class Meta:
        model = User 
        fields = ['first_name','last_name','username', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control', 'placeholder':'Enter new username'})
        self.fields['first_name'].widget.attrs.update({'class':'form-control', 'placeholder':'Enter new first name'})
        self.fields['last_name'].widget.attrs.update({'class':'form-control', 'placeholder':'Enter new last name'})
        self.fields['email'].widget.attrs.update({'class':'form-control', 'placeholder':'Enter your new email:'})

class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = User
        fields =  ['old_password','new_password','new_password1']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class':'form-control', 'placeholder':'Enter current password'})
        self.fields['new_password1'].widget.attrs.update({'class':'form-control', 'placeholder':'Enter old password'})
        self.fields['new_password2'].widget.attrs.update({'class':'form-control', 'placeholder':'Confirm password'})
        self.fields['old_password'].label = 'Current Password'
        


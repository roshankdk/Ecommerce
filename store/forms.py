from django.contrib.auth.forms import UserCreationForm, UserChangeForm
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


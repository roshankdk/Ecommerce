from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignupForm(UserCreationForm):
    # username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}))
    # password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    # password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control', 'placeholder':'Enter your username'})
        self.fields['password1'].widget.attrs.update({'class':'form-control', 'placeholder':'Create a password'})
        self.fields['password2'].widget.attrs.update({'class':'form-control', 'placeholder':'Confirm Password'})

    


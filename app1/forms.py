from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class signup_form(UserCreationForm):
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'username'}),label=("Username"),required=True)
    email = forms.CharField(max_length=100,widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}),label=("Email"),required=True)
    password1 = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}),label=("Password"))
    password2 = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'again password'}),label=("Password Confirmation"))
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class login_form(AuthenticationForm):
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'username'}),label=("Username"),required=True)
    password = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}),label=("Password"),required=True)
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import events

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

# class addevent_form(forms.ModelForm):
    # title = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}),label=("Title"),required=True)

    # description = forms.CharField(max_length=1000,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'description'}),label=("description"),required=True)

    # date = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control'}),label=("date"),required=True)

    # time = forms.TimeField(widget=forms.TimeInput(attrs={'class':'form-control','placeholder':'time'}))

    # poster = forms.ImageField(widget=forms.ImageField(attrs={'class':'form-control'}),label=("date"), required=True)


#     class Meta:
        # model = events
        # fields = ("title", "description", "date","time", "poster","duration")

class addevent_form(forms.ModelForm):
    title = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}),label=("Title"),required=True)
    description = forms.CharField(max_length=1000,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Description'}),label=("description"),required=True)
    # date = forms.DateTimeField(
    #     input_formats=['%d/%m/%Y %H:%M'],
    #     widget=forms.DateTimeInput(attrs={
    #         'class': 'form-control datetimepicker-input',
    #         'data-target': '#datetimepicker1'
    #     })
    # )
    date = forms.DateField(widget=forms.DateTimeInput(attrs={'class':'form-control datetimepicker-input','placeholder':'Date'}),label=("Date"),required=True)

    time = forms.TimeField(widget=forms.TimeInput(attrs={'class':'form-control','placeholder':'Time'}))

    poster = forms.ImageField()

    duration = forms.DurationField(required=True)

    class Meta:
        model = events
        fields = ("title", "description", "date","time","duration", "poster")

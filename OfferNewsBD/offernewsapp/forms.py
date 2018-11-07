from django import forms
from .models import Contact
from django.contrib.auth.forms import UserCreationForm  # Form for signup
from django.contrib.auth.models import User  # Django default user table


class ContactForm(forms.ModelForm):
    name = forms.CharField(required=True, max_length=30, label='', widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Your Name*"}))
    phn = forms.CharField(required=True, max_length=11, label='', widget=forms.NumberInput(attrs={"class":"form-control", "placeholder":"Mobile Number*"}))
    subject = forms.CharField(required=True, max_length=50, label='', widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Subject*"}))
    message = forms.CharField(required=True, max_length=250, label='', widget=forms.Textarea(attrs={"class":"form-control", "placeholder":"Message*"}))

    class Meta:
        model = Contact
        fields = ['name', 'phn', 'subject', 'message', ]


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter first name"}))
    last_name = forms.CharField(max_length=30, required=True,  widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter last name"}))
    email = forms.EmailField(max_length=254,required=True, help_text='Required. Inform a valid email address.',  widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Email"}))


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

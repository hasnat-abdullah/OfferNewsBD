from django import forms
from .models import Contact, Post, Category, Company,Coupon,Branch,FeaturedPost
from django.contrib.auth.forms import UserCreationForm  # Form for signup
from django.contrib.auth.models import User  # Django default user table

#-----------Post Ad-----------
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'comName', 'branch', 'category', 'offerType', 'AmountType', 'Amount', 'postImage', 'isFeatured', 'goingUrl', 'expiredOn',]


    title = forms.CharField(required=True, max_length=40, label='',widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Title*"}))
    description = forms.CharField(required=True, max_length=200, label='', widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Description*"}))
    comName = forms.ModelChoiceField(queryset=Company.objects.all(), empty_label="Select Store*",widget=forms.Select(attrs={"class": "form-control"}))
    branch = forms.ModelChoiceField(queryset=Branch.objects.all(), empty_label="Select Branch*",widget=forms.Select(attrs={"class": "form-control"}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Select Category*",widget=forms.Select(attrs={"class": "form-control"}))
    offerType = forms.ChoiceField(choices=Post.Offer_Type, widget=forms.Select(attrs={"class": "form-control", "placeholder": "Offer Amount*"}))
    AmountType = forms.ChoiceField(choices=Post.Amount_Type, widget=forms.Select(attrs={"class": "form-control", "placeholder": "Offer Amount*"}))
    Amount = forms.CharField(required=True, max_length=99, label='',widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Offer Amount*"}))
    postImage = forms.ImageField(required=True, label='', widget=forms.ClearableFileInput(attrs={"class": "form-control", "placeholder": "Offer Image*"}))
    expiredOn = forms.DateField(required=True, label='', widget=forms.DateInput(attrs={"style": "margin-bottom: 15px;", "class": "form-control datePickr", "placeholder": "Offer Expiry Date"}))
    goingUrl = forms.URLField(max_length=99, label='', widget=forms.URLInput(attrs={"class": "form-control", "placeholder": "Offer Url",}))
    isFeatured = forms.BooleanField(required=False,label='Feature This Offer', widget=forms.CheckboxInput(attrs={"class": "form-control","id":"isFeature", "name":"isFeature", "type":"checkbox", "onchange":"is_Feature(this)"}))



class CouponForm(forms.ModelForm):
    couponCode = forms.CharField(required=True, max_length=40, label='',widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Coupon Code*"}))

    class Meta:
        model = Coupon
        fields = [ 'couponCode',]


class FeaturedPostForm(forms.ModelForm):
    position = forms.ChoiceField(choices=FeaturedPost.Position_Type, widget=forms.Select(attrs={"class": "form-control"}))
    featuredExpireDate = forms.DateField(required=True, label='', widget=forms.DateInput(attrs={ "class": "form-control datePickr", "placeholder": "Feature Exp Date : dd/mm/yyyy"}))

    class Meta:
        model = FeaturedPost
        fields = [ 'position','featuredExpireDate',]


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

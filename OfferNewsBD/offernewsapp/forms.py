from django import forms
from .models import Post


class CreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'description',
            'comName',
            'category',
            'offerType',
            'AmountType'
            ,'Amount',
            'postImage',
            'goingUrl',
            'expiredOn',
            'couponCode',
            'isFeatured'
        ]
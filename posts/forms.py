from django import forms
from .models import review_post

class ReviewPostForm(forms.Form):
    title = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"placeholder": "Title"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Place your review here."}))
    poster = forms.CharField(max_length=30)

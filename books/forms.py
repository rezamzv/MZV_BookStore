from django import forms
from .models import Book

class BookForm(forms.Form):
    title  = forms.CharField(required=True, label="Title")
    author = forms.CharField(required=True, label="Author")
    category = forms.CharField(max_length=100, label="Category")
    price = forms.DecimalField(decimal_places=2, max_digits=10, label="Price")
    description = forms.CharField(required=True, label="Description")
    cover = forms.ImageField(required=True, label="Cover")

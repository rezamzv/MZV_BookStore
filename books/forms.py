from django import forms
from .models import Book

class BookForm(forms.Form):
    title  = forms.CharField(required=False, label="Title")
    author = forms.CharField(required=False, label="Author")
    category = forms.CharField(max_length=100, label="Category")
    price = forms.DecimalField(decimal_places=2, max_digits=10, label="Price")

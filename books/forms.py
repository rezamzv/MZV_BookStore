from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

from .models import Book,Comment

class BookForm(forms.Form):
    title  = forms.CharField(required=True, label="Title")
    author = forms.CharField(required=True, label="Author")
    category = forms.CharField(max_length=100, label="Category")
    price = forms.DecimalField(decimal_places=2, max_digits=10, label="Price")
    description = forms.CharField(required=True, label="Description")
    cover = forms.ImageField(required=True, label="Cover")

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment', 'rating']

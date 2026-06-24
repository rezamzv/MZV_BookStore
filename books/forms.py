from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

from .models import Book,Comment


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'category', 'price', 'description', 'cover',]



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment', 'rating']

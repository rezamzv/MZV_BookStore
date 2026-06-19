from django.shortcuts import render
from django.views import generic

from books.forms import BookForm
from books.models import Book


# Create your views here.
class HomePageView(generic.ListView):
    template_name = 'pages/home.html'
    model = Book
    context_object_name = 'books'
    form_class = BookForm
    paginate_by = 12




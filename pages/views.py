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

class CategoryListView(generic.ListView):
    template_name = 'pages/home.html'
    model = Book
    context_object_name = 'books'
    paginate_by = 12

    def get_queryset(self):
        category = self.kwargs.get('category')
        return Book.objects.filter(category=category)




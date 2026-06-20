from django.shortcuts import render
from django.template.context_processors import request
from django.views import generic
from django.db.models import Q

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


def search_list(request):
    query = request.GET.get('q','')
    books = Book.objects.all()
    if query:
        books = books.filter(
            Q(title__icontains=query) | Q(author__icontains=query) | Q(category__icontains=query)
        )
    return render(request, 'pages/search_list.html', {
        'books': books,
        'query': query,
    })






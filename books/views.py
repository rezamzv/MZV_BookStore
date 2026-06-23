from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy, reverse

from accounts.models import CustomUser
from books.forms import CommentForm
from books.models import Book, Comment


def book_detail_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book_comments = book.comments.all()

    if request.method == 'POST' and request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.author = request.user
            new_comment.book = book
            comment_form.save()
        comment_form = CommentForm()
    else:
        comment_form = CommentForm()


    return render(request, 'books/book_detail.html', {'book': book, 'comments': book_comments, 'comment_form': comment_form})


class BookCreateView(generic.CreateView):
    model = Book
    template_name = 'books/book_create.html'
    fields = '__all__'


class BookUpdateView(generic.UpdateView):
    model = Book
    template_name = 'books/book_update.html'
    fields = '__all__'


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')

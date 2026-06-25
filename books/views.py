from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from books.forms import CommentForm, BookForm
from books.models import Book, Comment, WishList


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/book_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # comments
        context['comment_form'] = CommentForm()
        context['comments'] = self.object.comments.all()

        # wishlist
        if self.request.user.is_authenticated:
            context['added'] = WishList.objects.filter(
                user=self.request.user,
                book=self.object
            ).exists()

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.book = self.object
            comment.save()

        return self.get(request, *args, **kwargs)


class BookCreateView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = Book
    template_name = 'books/book_create.html'
    fields = ['title', 'author', 'price', 'cover', 'category', 'description', ]
    success_url = reverse_lazy('home_page')

    def test_func(self):
        return self.request.user.is_staff

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Book
    template_name = 'books/book_update.html'
    fields = '__all__'

    def test_func(self):
        book = self.get_object()
        return book.created_by == self.request.user


class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('home_page')

    def test_func(self):
        book = self.get_object()
        return book.created_by == self.request.user


@login_required
def toggle_wishlist(request, pk):
    book = get_object_or_404(Book, pk=pk)
    wishlist_item, created = WishList.objects.get_or_create(user=request.user, book=book)
    added = True
    if not created:
        wishlist_item.delete()  # already in wishlist → remove it
        added = False
    print(added)
    return redirect('book_detail', pk=pk)


class WishListView(LoginRequiredMixin, generic.ListView):
    model = WishList
    template_name = 'books/wishlist.html'
    context_object_name = 'wishlists'

    def get_queryset(self):
        return WishList.objects.filter(user=self.request.user)

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic

from books.models import Book
from cart.models import Cart


@login_required
def add_to_cart(request, pk):
    book = get_object_or_404(Book, pk=pk)
    item, created = Cart.objects.get_or_create(user=request.user, book=book)
    if created:
        item.quantity = 1
    else:
        item.quantity += 1
    item.save()
    return redirect('book_detail', pk=book.pk)


def add_one_to_cart(request, pk):
    book = get_object_or_404(Book, pk=pk)
    item, created = Cart.objects.get_or_create(user=request.user, book=book)
    if not created:
        item.quantity += 1
        item.save()
    return redirect('cart')


def remove_one_from_cart(request, pk):
    book = get_object_or_404(Book, pk=pk)
    item, created = Cart.objects.get_or_create(user=request.user, book=book)
    if not created:
        item.quantity -= 1
        item.save()
        if item.quantity <= 1:
            item.delete()

    return redirect('cart')


@login_required
def remove_from_cart(request, pk):
    Cart.objects.filter(user=request.user, book_id=pk).delete()
    return redirect('cart')


class CartView(LoginRequiredMixin, generic.ListView):
    model = Cart
    template_name = 'cart/cart.html'
    context_object_name = 'items'

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total'] = sum(i.total for i in self.get_queryset())  # ← uses the property

        return context

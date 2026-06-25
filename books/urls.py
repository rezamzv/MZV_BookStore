from django.urls import path

from books.views import BookDetailView, BookCreateView, BookUpdateView, BookDeleteView, WishListView, toggle_wishlist

urlpatterns = [
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('create/', BookCreateView.as_view(), name='book_create'),
    path('<int:pk>/update/', BookUpdateView.as_view(), name='book_update'),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
    path('wishlist/', WishListView.as_view(), name='wishlist'),
    path('wishlist/toggle/<int:pk>/', toggle_wishlist, name='toggle_wishlist'),
]

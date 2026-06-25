from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models

from books.models import Book
from config import settings


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    @property
    def total(self):
        return self.quantity * self.book.price


    class Meta:
        unique_together = ['user', 'book']
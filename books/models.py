from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
import os

from accounts.models import CustomUser


def rename_image(instance, filename):
    ext = filename.split('.')[-1]  # get the original extension (jpg, png, etc.)
    new_filename = f"{slugify(instance.title)}.{ext}"
    return os.path.join('covers/', new_filename)


class Book(models.Model):
    CATEGORY_CHOICES = [
        ('fiction', 'Fiction'),
        ('nonfiction', 'Non-Fiction'),
        ('fantasy', 'Fantasy'),
        ('classics', 'Classics'),
        ('education', 'Education'),
        ('children', 'Children'),
    ]

    class Meta:
        ordering = ['-created_at']  # the minus sign = descending = newest first

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.TextField(max_length=500)
    cover = models.ImageField(upload_to=rename_image, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    class Meta:
        ordering = ['-created_at']
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )


class WishList(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='wishlist')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='wishlisted_by')
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'book']  # ← prevent duplicate entries

    def __str__(self):
        return f"{self.user} - {self.book}"
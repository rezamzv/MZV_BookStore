from django.db import models
from django.urls import reverse

class Book(models.Model):
    CATEGORY_CHOICES = [
        ('fiction', 'Fiction'),
        ('nonfiction', 'Non-Fiction'),
        ('fantasy', 'Fantasy'),
        ('classics', 'Classics'),
        ('education', 'Education'),
        ('children', 'Children'),
        ('new_arrivals', 'New Arrivals'),
    ]

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse ('book_detail', kwargs={'pk': self.pk})

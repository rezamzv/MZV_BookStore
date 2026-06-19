from django.db import models
from django.urls import reverse
from django.utils.text import slugify
import os

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
        ('new_arrivals', 'New Arrivals'),
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


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse ('book_detail', kwargs={'pk': self.pk})

from django.contrib import admin

from books.models import Book

# Register your models here.
admin.site.register(Book)

class BookAdmin(admin.ModelAdmin):
    fieldsets = ['title', 'author', 'price', 'category']
    display = ['title', 'author', 'price', 'category']

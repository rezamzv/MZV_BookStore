from django.contrib import admin

from books.models import Book, Comment


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'category', 'price','created_by', 'created_at')
    ordering = ('-id',)
    search_fields = ('title',)
    list_per_page = 20


@admin.register(Comment)
class Comments(admin.ModelAdmin):
    list_display = ('author', 'comment', 'created_at')

from django.contrib import admin


from books.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','author','category' ,'price','created_at')
    ordering = ('-id',)
    search_fields = ('title',)
    list_per_page = 20


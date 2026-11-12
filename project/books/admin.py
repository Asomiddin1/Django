from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "price")
    search_fields = ("title", "author" , "created_at")
    ordering = ("title", "author")
    list_filter = ("author", "price")
    
admin.site.register(Book, BookAdmin)
 
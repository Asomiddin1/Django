from django.contrib import admin
from .models import Book, Students


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "price")
    search_fields = ("title", "author" , "created_at")
    ordering = ("title", "author")
    list_filter = ("author", "price")

class StudentsAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "group")
    search_fields = ("name", "group")
    ordering = ("name", "group")
    list_filter = ("group", "age")
    
admin.site.register(Book, BookAdmin)
admin.site.register(Students, StudentsAdmin)
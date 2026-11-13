from django.contrib import admin
from .models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email', 'enrollment_date')
    search_fields = ('name', 'email')
    list_filter = ('enrollment_date',)

admin.site.register(Student, StudentAdmin)
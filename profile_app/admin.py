from django.contrib import admin
from .models import StudentProfile

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'program', 'year', 'gpa')
    list_filter = ('program', 'year')
    search_fields = ('name',)

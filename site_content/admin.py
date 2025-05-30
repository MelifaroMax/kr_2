from django.contrib import admin
from .models import PageContent

@admin.register(PageContent)
class PageContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'image')
    search_fields = ('title',)


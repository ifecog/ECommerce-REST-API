from django.contrib import admin
from django.utils.html import format_html

from .models import Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.image.url))
    
    thumbnail.short_description = 'photo'

    list_display = ('_id', 'thumbnail', 'name')
    list_display_links = ('name', 'thumbnail')
    search_fields = ['name', 'description']


admin.site.register(Category, CategoryAdmin)
    
    

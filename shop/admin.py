from typing import Any
from django.contrib import admin
from django.http.request import HttpRequest
from django.utils.html import format_html

from .models import Category, Brand, Product, Review

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.image.url))
    
    thumbnail.short_description = 'photo'

    list_display = ('_id', 'thumbnail', 'name')
    list_display_links = ('name', 'thumbnail')
    search_fields = ['name', 'description']


class BrandAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        try:
            return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.image.url))
        except:
            pass
    
    thumbnail.short_description = 'photo'

    list_display = ('_id', 'thumbnail', 'name')
    list_display_links = ('name', 'thumbnail')
    search_fields = ['name', 'description']


class ProductAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.image.url))
    
    thumbnail.short_description = 'photo'

    list_display = ('_id', 'thumbnail', 'name', 'category', 'brand', 'price', 'quantity', 'rating')
    list_display_links = ('name', 'thumbnail')
    search_fields = ['name', 'category', 'description']
    
    # def save_model(self, request, obj, form, change):
    #     # Only allow admin users to set the user field when creating a product
    #     if not obj.pk and request.user.is_superuser:
    #         obj.user = request.user
                    
    #     super().save_model(request, obj, form, change)
    
    # def has_add_permission(self, request):
    #     # only allow admin users to add products
    #     return request.user.is_superuser


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['_id', 'name', 'product', 'rating']
    list_display_links = ['_id', 'name', 'product']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)    
admin.site.register(Review, ReviewAdmin)
    

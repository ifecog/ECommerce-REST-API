from typing import Any
from django.db import models
from users.models import CustomUser

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/categories/', null=True)
    _id = models.AutoField(primary_key=True, editable=False)
    
    class Meta:
        verbose_name_plural = 'categories'
        
    def __str__(self):
        return self.name
    
    
class Brand(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/brands/', null=True)
    _id = models.AutoField(primary_key=True, editable=False)
    
       
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='uploads/products/', null=True, blank=True, default='/placeholder.png')
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True, default=0)
    is_fragile = models.BooleanField(default=False)
    rating = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    no_of_reviews = models.IntegerField(null=True, blank=True, default=0)
    created_time = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        # check if category is Electronics
        if self.category and self.category.name in ['Electronics',]:
            self.is_fragile = True
        else:
            self.is_fragile = False
            
        print(f"Category: {self.category.name}, is_fragile: {self.is_fragile}")    
        
        super().save(*args, **kwargs)
    
    
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True, default=0)
    comment = models.TextField(null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)
    
    def __str__(self):
        return str(self.rating)
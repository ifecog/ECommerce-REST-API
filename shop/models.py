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

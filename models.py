# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# Product model
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Lead(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    interested_product = models.ManyToManyField(Product, related_name='leads')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



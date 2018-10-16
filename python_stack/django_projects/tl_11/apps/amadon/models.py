
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

# Product.objects.create(product_name="Polo Shirt", unit_price=79.99)
# Product.objects.create(product_name="Baseball Cap", unit_price=15.00)
# Product.objects.create(product_name="Wool Scarf", unit_price=10.99)
# Product.objects.create(product_name="Running Shoes", unit_price=74.99)
# Product.objects.create(product_name="Football Jersey", unit_price=149.99)

from tokenize import blank_re
from django.db import models
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):

    category_choice = (
        ('Clothes', 'Clothes'),
        ('Objects', 'Objects'),
        ('Sticker', 'Sticker'),
        ('Book', 'Book'),
        ('Poster', 'Poster'),
    )
    size_choice = (
        ('L', 'L'),
        ('M', 'M'),
        ('S', 'S'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
        ('Child 11-13', 'Child 11-13'),
        ('Child 3-4', 'Child 3-4'),
        ('Child 5-6', 'Child 5-6'),
        ('Child 7-8', 'Child 7-8'),
        ('Child 9-10', 'Child 9-10'),
    )

    product_name = models.CharField(max_length=255)
    category = models.CharField(choices=category_choice, max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    decription_product = RichTextField()
    photo_principal = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_principal_2 = models.ImageField(
    upload_to='photos/%Y/%m/%d/', blank=True)
    photo_principal_3 = models.ImageField(
    upload_to='photos/%Y/%m/%d/', blank=True)
    photo_principal_4 = models.ImageField(
    upload_to='photos/%Y/%m/%d/', blank=True)
    quantity = models.IntegerField(default=0)
    sizes_for_clothes = MultiSelectField(choices=size_choice, blank=True)
    rating = models.IntegerField(default=0, blank=True)
    review = RichTextField(blank=True)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)
    total_payment = models.DecimalField(default=0,max_digits=7, decimal_places=2)

    def __str__(self):
        return str(self.total_payment)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    size =  models.CharField(default="",max_length=255)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


class ShippingAddress(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

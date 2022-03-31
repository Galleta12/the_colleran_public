from itertools import product
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import JsonResponse
from asgiref.sync import sync_to_async
from time import sleep
import asyncio
import json
import stripe

stripe.api_key = "sk_test_51KgakrAp4AtDjyoPpNK8qP03epbzs0FyPjZz8f4mWYE3GovVzdb66SL5o1KnM6l85zeKvXfGSMReqOrA2FfIFRlM00Wltbv78F"

# Create your views here.
def products(request):
   products_db = Product.objects.filter(is_featured = True)
   data = {
      'products_db': products_db,
   } 
   return render(request, 'products/products.html', data)

def products_details(request,id):
   single_product = get_object_or_404(Product, pk = id)
   data = {
      "single_product" : single_product,
   }
        
   return render(request,'products/products_details.html', data)


def cart(request):
   
   if request.user.is_authenticated:
      customer = request.user
      order, created = Order.objects.get_or_create(customer=customer,complete=False)
      items= order.orderitem_set.all()
   else:
      messages.error(request, 'You need to log in first')
      return redirect('login')
   data = {'items': items}
   
   
   return render(request,'products/cart.html',data)
     
 

def updateItem(request):
   if request.user.is_authenticated:
      data = json.loads(request.body)
      productId = data['productId']
      action = data['action']
      category = data['category']
      size = data['size']
      
      print('Action: ', action)
      print('ProductId: ', productId)
      print('Category: ', category)
      print('Size: ', size)
      
      customer = request.user
      product = Product.objects.get(id=productId)
      
      if product.category == "Clothes" and not size:
         
         return JsonResponse('Item was not added', safe=False)
      else:
      
         order, created = Order.objects.get_or_create(customer=customer,complete=False)
         if product.category == "Objects":
            orderItem, created = OrderItem.objects.get_or_create(order=order,product=product)
         elif product.category == "Clothes":
            orderItem, created = OrderItem.objects.get_or_create(order=order,product=product,size=size)
         
         if action == 'add':
            orderItem.quantity= (orderItem.quantity + 1)
         elif action == 'remove':
            orderItem.quantity= (orderItem.quantity - 1)
         orderItem.save()
         
         if orderItem.quantity <= 0:
            orderItem.delete()
         return JsonResponse('Item was added', safe=False)
   else:
      return redirect('login')

def open_checkout(request):
   
   if request.user.is_authenticated:
      
      customer = request.user
      order, created = Order.objects.get_or_create(customer=customer,complete=False)
      
      items= order.orderitem_set.all()
      data = {
      'orderItem': items,
      'order': order,
         }
      print(data)
      return render(request,'products/open_checkout.html',data)


def save_total_payment(request):
   if request.user.is_authenticated:
      data = json.loads(request.body)
      total_pay = data['total_pay']

      customer = request.user
      order = Order.objects.get(customer = customer)
      order.total_payment = total_pay
      order.save()
     # print(total_pay)
      return JsonResponse('Item was added', safe=False)
   

def charge(request):
   
   
   if request.method == 'POST':
      print('Data:', request.POST)
      amounts = request.POST['amount']
      amountss= int(float(amounts)) * 100
     
      
      customer = stripe.Customer.create(
			email=request.POST['email'],
			name=request.POST['nickname'],
         source=request.POST['stripeToken']
		)
      charge = stripe.Charge.create(
			customer=customer,
			amount=amountss,
			currency='gbp',
			description="Donation"
		)
      return JsonResponse('Hello', safe=False)
     




   

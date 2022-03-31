from django.shortcuts import render
from products.models import Product
from what_we_dos.models import What_DO

# Create your views here.

def home(request):
    products_db = Product.objects.order_by('-price')[:3]
    
    data = {
        'products_db': products_db,
    }
    what_dos = What_DO.objects.filter(is_featured = True)
    data1 = {
        'what_dos': what_dos,
    } 
    
    
    return render(request, 'pages/home.html', context ={'data':data, 'data1':data1})


def about(request):
    return render (request, 'pages/about_bobby.html')
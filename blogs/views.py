from django.shortcuts import render
from .models import *
# Create your views here.

def blogs(request):
    blogs_db = Blog.objects.filter(is_featured = True)
    
    data = {
        'blogs_db': blogs_db,
    }
    return render(request, 'blogs/blogs.html', data)
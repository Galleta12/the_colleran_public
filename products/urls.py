from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('<int:id>', views.products_details, name='products_details'),
    path('cart', views.cart, name='cart'),
    path('update_item/', views.updateItem, name='update_item'),
    path('open_checkout/', views.open_checkout, name='open_checkout'),
    path('save_total_payment/', views.save_total_payment, name='save_total_payment'),
    path('charge/', views.charge, name='charge'),
    
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.what_we_dos, name='what_we_dos'),
    path('<int:id>',views.what_do_details,name='what_do_details'),
   
]

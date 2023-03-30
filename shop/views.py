from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect
from . models import Product, Category
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect 
from django.views.generic import ListView 
from django.views  import generic  

class Home(ListView):
    model = Category
    template_name = 'home.html'
   
class Category(generic.ListView):
    model = Product
    template_name = 'category.html'

    #def category(self , request , id_cat ):
    #   cat_name = self.Category.objects.get(category = id_cat)
    #   data = self.Product.objects.filter(category = id_cat)
    #   return render(request , self.template_name  , {'data': data , "name": cat_name.name } )
  
class Product(ListView ):
    model = Product
    template_name = 'product.html'

def base(request):
    return render( request , "shop/base.html" )


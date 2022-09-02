from django.shortcuts import render,get_object_or_404,redirect
from .models import Product
from category.models import Category

def store(request,category_slug=None):

    category=None
    products=None
    if category_slug !=None:
        category=get_object_or_404(Category.objects.prefetch_related("product_set"),slug=category_slug)
        products=category.product_set.all().filter(is_av=True).select_related("category")
    else:
     products=Product.objects.all().filter(is_av=True).select_related("category")

    
    contex={    
        'products':products
    }
    return render(request,"store/store.html",contex)


def product_detail(request,category_slug,product_slug):

    category=get_object_or_404(Category,slug=category_slug)
    if category:
        product=get_object_or_404(Product.objects.select_related("category"),category=category,slug=product_slug)
    
    contex={
        'product':product
    }
    return render(request,"store/product_detail.html",contex)














def all_store(request):

    products=Product.objects.all().filter(is_av=True).select_related("category")
    contex={    
        'products':products
    }
    return render(request,"store/all-store.html",contex)
from django.shortcuts import render,get_object_or_404,redirect
from django.http import Http404
from .models import Category

def categories(request):

    cats=Category.objects.prefetch_related("product_set").all()
    contex={
        'cats':cats
    }
    return contex
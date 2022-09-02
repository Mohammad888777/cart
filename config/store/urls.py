from django.urls import path
from . import views

urlpatterns=[
    path("",views.all_store,name="all_store"),
    path("<slug:category_slug>/",views.store,name="store"),
    path("<slug:category_slug>/<slug:product_slug>/",views.product_detail,name="product_detail"),
]

    # 
# 
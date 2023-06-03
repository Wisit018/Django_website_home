from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def foods(request):
    return render(request, "app_shop/shop.html")

def food(request, shop_id):
    return render(request, "app_shop/idshop.html", {"shop_id": shop_id})
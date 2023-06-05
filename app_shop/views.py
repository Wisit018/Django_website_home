from django.http.response import HttpResponse
from django.shortcuts import render

all_shops = [
    {"id": 1, "title": "Ex1-Name", "price": 100, "is_premium" : True},
    {"id": 2, "title": "Ex2-Name", "price": 100, "is_premium" : False},
    {"id": 3, "title": "Ex3-Name", "price": 100, "is_premium" : True},
    
]

# Create your views here.
def foods(request):
    context = {"all_shops": all_shops}
    return render(request, "app_shop/shop.html", context)

def food(request, shop_id):
    return render(request, "app_shop/idshop.html", {"shop_id": shop_id})
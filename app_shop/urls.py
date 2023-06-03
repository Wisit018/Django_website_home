from django.urls import path
from . import views

urlpatterns = [
    path('', views.foods, name='shops'),
    path('<int:shop_id>/', views.food, name='shops'),
]
    
    
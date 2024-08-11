from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'admin'

urlpatterns = [
    path('',admin_login,name="admin_login_view"),
    path('logout/',admin_logout,name="admin_logout"),
    path("dashboard",dashboard,name="dashboard"),
    path("restaurant/",restaurant,name="restaurant"),
    path("users/",users,name="users"),
    path("carousel_images/",carousel_images,name="carousel_images"),
    path("menu/",menu,name="menu"),
    path("orders/",orders,name="orders"),
    path("daily_offers/",daily_offers,name="daily_offers"),
]

from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name="home"),
    path('menu/',menu,name="menu"),
    path('gallery/',gallery,name="gallery"),
    path('orders/<int:id>',orders,name="orders"),
    path('reservation/',reservation,name="reservation"),
    path('login/',login_view,name="login_view"),
    path('logout/',logout_view,name="logout_view"),
    path('signup/',signup,name="signup"),
]



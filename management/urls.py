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
    path("change_password/", change_password, name="change_password"),
    path("profile/<int:id>", profile, name="profile"),
]



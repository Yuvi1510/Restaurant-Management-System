from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from management.models import *
# Create your views here.
def dashboard(request):
    return render(request,'admin/dashboard.html')

def restaurant(request):
    if request.method=='POST':
        res_id=request.POST.get("restaurant_id")
        name = request.POST.get("name")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        instagram = request.POST.get("instagram")
        facebook = request.POST.get("facebook")
        logo = request.FILES.get("logo")

        restaurant = MainInfo.objects.get(id=res_id)
        restaurant.name = name
        restaurant.address = address
        restaurant.phone = phone
        restaurant.email = email
        restaurant.instagram = instagram
        restaurant.facebook = facebook

        if logo:
            restaurant.logo= logo
        restaurant.save()
    return render(request,"admin/restaurant.html",{"infos":MainInfo.objects.all()})


def users(request):
    users=User.objects.filter(is_superuser=True)
    profiles=UserProfile.objects.all()
    return render(request,"admin/users.html",{"users":users,"profiles":profiles})

def carousel_images(request):
    if request.method == "POST":
        image_id = request.POST.get("image_id")
        if image_id:
            image = CarouselImages.objects.filter(id=image_id)
            image.delete()
            messages.success(request,"Image successfully deleted")
        else:
            carousel_image = request.FILES.get("carousel_image")
            if carousel_image:
                cImage=CarouselImages.objects.create(image = carousel_image)
                cImage.save()
                messages.success(request,"Image added successfully")
            else:
                messages.warning(request,"Please select an image file") 
    context ={'cImages': CarouselImages.objects.all()}
    return render(request,"admin/carousel_images.html",context)
def menu(request):
    return render(request,"admin/menu_list.html")
def orders(request):
    return render(request,"admin/orders_list.html")
def daily_offers(request):
    return render(request,"admin/daily_offers.html")

def admin_login(request):
    try:
        if request.user.is_authenticated:
            return redirect("dashboard")

        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")

            user_obj = User.objects.filter(username = username)

            if not user_obj.exists():
                messages.error(request,"User not found")
                return redirect("admin_login_view")
            
            user_obj = authenticate(username=username, password=password)

            if user_obj and user_obj.is_superuser:
                login(request,user_obj)
                return redirect("dashboard")
            messages.info(request,"Invalid credentials")
            return redirect("admin_login")
        
        return render(request, "admin/login.html")
            
    except Exception as e:
        print(e)


def admin_logout(request):
    logout(request)
    return redirect("admin_login")

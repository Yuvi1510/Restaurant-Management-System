from django.shortcuts import render, redirect, get_object_or_404
from .models import *
import random
from django.contrib import messages
from .models import UserProfile , Order
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    carousel_images = CarouselImages.objects.all()
    daily_offers = DailyOffer.objects.all()

    items = Items.objects.all()
    
    items_length = len(items)
    selected_items = []
    n=0
    if items_length < 6:
        n = items_length
    else:
        n = 6
    while len(selected_items) < n:
        i=random.randint(0,items_length-1)
        item = items[i]
        if item not in selected_items:
            selected_items.append(item)
            
    return render(request,'home.html',{
        'carousel_images':carousel_images,
        "daily_offers":daily_offers,
        'items_list':selected_items,
        })


def menu(request):
    menu = Menu.objects.all()
    items = Items.objects.all()
    return render(request,"menu.html",{'menu': menu, 'items':items})

def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "password does not match!")
            return redirect('signup')

        
        if User.objects.filter(email=email).exists():
            messages.info(request, "This email is already used!")
            return redirect('signup')
        
        user = User.objects.create(username=email,email=email, first_name=first_name, last_name=last_name)
        user.set_password(password2)
        user.save()
        user_profile=UserProfile.objects.create( profile=user,first_name=first_name,last_name=last_name, email=email, phone=phone_number)
        user_profile.save()
        login(request,user)
        return redirect('home')
        

    return render(request,"signup.html")

def login_view(request):
    if request.method=='POST':
        user_email = request.POST.get('email')
        user_password = request.POST.get('password')
        user = authenticate( username = user_email, password=user_password)
        print(user)
        if user is not None:
            login(request, user)
            messages.success(request,"Login successful!")
            return redirect('home')
        else:
            messages.error(request,"Login failed")
    return redirect('home')

def logout_view(request):
    logout(request)
    return redirect('home')

def profile(request, id):
    user = get_object_or_404(User, id=id)
    print(user)
    user_profile =UserProfile.objects.filter(profile=request.user)
    return render(request, 'profile.html',{'user_profile':user_profile})

@login_required
def change_password(request):
    if request.method == 'POST':
        old_password = request.POST.get("old_password")
        new_password1 = request.POST.get("new_password1")
        new_password2 = request.POST.get("new_password2")

        if not request.user.check_password(old_password):
            messages.error(request, "Old password is incorrect!")
            return redirect('change_password')
        elif new_password1 != new_password2:
            messages.error(request, "New password did not match")
            return redirect('change_password')
        else:
            request.user.set_password(new_password1)
            request.user.save()
            messages.success(request,"Password changed successfully")
            return redirect("home")
    return render(request, "change_password.html")





def gallery(request):
    return render(request,"gallery.html")


def orders(request,id):
    user_id = get_object_or_404(User,id=id)
    user_profile = UserProfile.objects.filter(profile=user_id)
    orders = Order.objects.filter(order_from= user_profile.first(), completed=False)
    # print(f'orders: {orders}')
    if request.method=='POST':
        item = request.POST.get("item")
        item=Items.objects.filter(name=item).first()
        if item is None:
            messages.error(request,"Please select an item!")
            return redirect('orders', id=id)
        # print(item)
        if not orders.exists():
            print("None")
            orders= Order.objects.create(order_from=user_profile.first(),completed=False)
            orders.save()
            quantity=1
            order_list=OrderList.objects.create(order_list_of=orders,item=item,quantity=quantity,total=item.price)
            order_list.save()
        else:
           print("not none")
           order_list= OrderList.objects.filter(order_list_of=orders.first())
           item_found_in_list = True
           for order in order_list:
               print(f'matching {order.item} and {item}')
               if str(order.item).upper() == str(item).upper():
                    order.quantity+=1
                    order.total+= item.price
                    order.save()
                    print("order updated")
                    item_found_in_list = True
                    break
               else:
                   item_found_in_list = False
            
           if item_found_in_list==False:
               order_list=OrderList.objects.create(order_list_of=orders.first(),item=item,quantity=1,total=item.price)
               order_list.save()
               print("item added to order")
                   
           
    context ={}
    processing_order_item_lists=[]
    completed_order_item_lists=[]

    # user profile object

    context.update({'orders':orders})
    try:
        orders = Order.objects.filter(order_from= user_profile.first())
        for order in orders:
            item_list = OrderList.objects.filter(order_list_of = order)
            if order.completed:
                completed_order_item_lists.append(item_list)
            else:
                processing_order_item_lists.append(item_list)
        
        context.update({"processing_order_item_lists":processing_order_item_lists,
                    "completed_order_item_lists":completed_order_item_lists})
   
        print(context)
        return render(request,'orders.html',context)
    except Exception as e:
        print(e)
        return render(request,'orders.html',context)

def reservation(request):
    return render(request,"reservation.html")


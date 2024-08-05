from django.contrib import admin
from .models import *

class ItemsInline(admin.StackedInline):
    model = Items
    extra = 1
    
class MenuAdmin(admin.ModelAdmin):
    inlines=[ItemsInline]

class OrderListInline(admin.StackedInline):
    model = OrderList
    extra =1
    

class OrderAdmin(admin.ModelAdmin):
    inlines=[OrderListInline]


# Register your models here.
admin.site.register(MainInfo)
admin.site.register(CarouselImages)
admin.site.register(Menu,MenuAdmin)
admin.site.register(DailyOffer)
admin.site.register(Items)
admin.site.register(UserProfile)
admin.site.register(Order,OrderAdmin)

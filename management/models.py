from django.db import models
from django.core import validators
from django.core.validators import MinLengthValidator,MaxLengthValidator,MinValueValidator,MaxValueValidator
from .costume_validators import digits_validation
from django.contrib.auth.models import User
# Create your models here.
class MainInfo(models.Model):
    name= models.CharField(max_length=20)
    logo = models.ImageField(upload_to='images/')
    address = models.CharField(max_length=30)
    phone = models.CharField(max_length=10,validators=[MinLengthValidator(10),MaxLengthValidator(10),digits_validation])
    email = models.EmailField()
    facebook = models.URLField()
    instagram = models.URLField()

    def __str__(self):
        return self.name
    
    class Meta:
          verbose_name_plural = 'Main Informations'
    

class CarouselImages(models.Model):
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return "image"
    class Meta:
          verbose_name_plural = 'Carousel Images'


class Menu(models.Model):
     category = models.CharField(max_length=50)
     
     def __str__(self):
          return self.category 

class Items(models.Model):
     category = models.ForeignKey(Menu,on_delete=models.CASCADE)
     image = models.ImageField(upload_to='images/')
     name = models.CharField(max_length=50)
     description = models.TextField(max_length=30)
     price = models.FloatField(validators=[MinValueValidator(0)])
    
     def __str__(self):
        return self.name 
     class Meta:
          verbose_name_plural = 'Items'

class DailyOffer(models.Model):
        item=models.ForeignKey(Items,on_delete=models.CASCADE)
        discount = models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(100)])
        price = models.FloatField(null = True, blank=True)

        @property
        def discounted_price(self):
            # Calculate and return the discounted price
            return self.item.price * (1 - (self.discount / 100))

        def save(self, *args, **kwargs):
            # Set the price field to the discounted price before saving
            self.price = self.discounted_price

            # Call the original save method
            super(DailyOffer, self).save(*args, **kwargs)
        
        def __str__(self):
             return self.item.name
        
        verbose_name_plural = 'Daily Offers'

class UserProfile(models.Model):
     profile = models.OneToOneField(User, on_delete=models.CASCADE)
     first_name = models.CharField(max_length=20)
     last_name = models.CharField(max_length=20)
     email = models.EmailField()
     phone = models.CharField(max_length=10,validators=[MinLengthValidator(10),MaxLengthValidator(10),digits_validation])
     remember_me = models.BooleanField(default=False)

     def __str__(self):
          return self.profile.first_name
     

class Order(models.Model):
     order_from = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
     total = models.FloatField(default=0)
     completed = models.BooleanField(default=False)
     paid = models.BooleanField(default=False)
     def __str__(self):
          return self.order_from.first_name
     class Meta:
          ordering = ['completed','id'] # Orders by 'completed' first, then by 'id'

class OrderList(models.Model):
     order_list_of = models.ForeignKey(Order,on_delete=models.CASCADE)
     item = models.ForeignKey(Items,on_delete=models.CASCADE)
     quantity = models.IntegerField(validators=[MinValueValidator(0)],default=0)
     total = models.FloatField(default=0)
     
     def __str__(self):
          return self.item.name
     
     @property
     def total_price(self):
        return self.item.price*self.quantity
          
     def save(self, *args, **kwargs):
          self.total = self.total_price
          super(OrderList,self).save(*args,**kwargs)

     
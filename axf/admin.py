from django.contrib import admin
from .models import Wheel,Nav,Mustbuy,Shop,MainShow,FoodTypes,Goods,User,Cart,Order
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'userAccount', 'userPasswd',]

admin.site.register(User, UserAdmin)


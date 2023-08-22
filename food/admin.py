from django.contrib import admin
from .models import Cuisine 
from .models import Food
from .models import Order

class CuisineAdmin(admin.ModelAdmin):
    list_display = ('category','created_at')
    ordering =('category',)

class FoodAdmin(admin.ModelAdmin):
    list_display =('name' ,'price','is_available')
    ordering = ('name',)
    list_editable = ('is_available',)
    search_fields = ('name',)
    list_filter = ('is_available',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','user','order_details','is_ready' , 'is_delivered')
    list_editable = ('is_ready' , 'is_delivered')
    ordering = ('-id',)

#admin.site.register(Cuisine)
admin.site.register(Cuisine , CuisineAdmin)
admin.site.register(Food , FoodAdmin)
admin.site.register(Order , OrderAdmin)

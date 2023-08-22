from django.urls import path


from . import views

urlpatterns = [
    path('menu/',views.menu , name="menu"),
    path('details/<int:id>', views.details , name="details"),
    path('add_to_cart/', views.add_to_cart , name="add_to_cart"),
    path('cart/' , views.cart , name="cart"),
    path('delete_cart_item/<str:id>/' , views.delete_cart_item , name="delete_cart_item"),
    path('checkout/' , views.checkout , name="checkout"),
    path('place_order/' , views.place_order , name="place_order"),
    path('orders/' , views.orders , name="orders"),
] 
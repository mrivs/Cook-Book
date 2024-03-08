from django.urls import path
from .import views

urlpatterns = [
 path('', views.main, name='main'),
#  path('client_form/', views.client_form, name='client_form'),
#  path('client_orders/<int:client_id>/', views.client_orders,
# name='client_orders'),
#  path('order_full/<int:order_id>/', views.order_full, name='order_full'),
 

# path('product_form/', views.product_form, name='product_form'),
# path('product_list/', views.product_list, name='product_list'),
]
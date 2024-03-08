from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.
import logging
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime, timedelta
# from .models import Order, Client, Product
# from .forms import ClientForm, ProductForm



def main(request):
    # clients = Client.objects.all()
    context = {"title": "main page"}

    return render(request, "app_cookbook/main.html", context)


# def client_orders(request, client_id):
#     client = get_object_or_404(Client, pk=client_id)

#     orders_7_days = Order.objects.filter(
#         client=client, date_ordered__gte=datetime.now() - timedelta(days=7)
#     ).order_by("-date_ordered")
#     orders_30_days = Order.objects.filter(
#         client=client, date_ordered__gte=datetime.now() - timedelta(days=30)
#     ).order_by("-date_ordered")
#     orders_365_days = Order.objects.filter(
#         client=client, date_ordered__gte=datetime.now() - timedelta(days=365)
#     ).order_by("-date_ordered")

#     context = {
#         "client": client,
#         "orders_7_days": orders_7_days,
#         "orders_30_days": orders_30_days,
#         "orders_365_days": orders_365_days,
#     }

#     return render(request, "myapp/client_orders.html", context)


# def order_full(request, order_id):

#     order = get_object_or_404(Order, pk=order_id)
#     products = Product.objects.filter(order=order)
#     context = {"products": products, "order": order}
#     return render(request, "myapp/order_full.html", context)


# def client_form(request):

#     if request.method == "POST":
#         form = ClientForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("client_form")
#     else:
#         form = ClientForm()
#     context = {"form": form}
#     return render(request, "myapp/client_form.html", context)
# Create your views here.

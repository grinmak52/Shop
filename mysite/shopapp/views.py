from timeit import default_timer
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy

from .models import Product, Order
from .forms import OrderForm


def shop_index(request):
    products = [
        ("Laptop", 1999),
        ("Desktop", 2999),
        ("Smartphone", 999),
    ]
    context = {"time_running": default_timer(), "products": products}
    return render(request, "shopapp/shop-index.html", context=context)


def groups_list(request):
    context = {
        "groups": Group.objects.prefetch_related("permissions").all(),
    }
    return render(request, "shopapp/groups-list.html", context=context)


class ProductsListView(ListView):
    model = Product
    template_name = "shopapp/products-list.html"
    context_object_name = "products"


class ProductDetailView(DetailView):
    template_name = "shopapp/product-detail.html"
    model = Product
    context_object_name = "product"


class ProductCreateView(CreateView):
    template_name = "shopapp/product-create.html"
    model = Product
    fields = "name", "price", "description", "discount"
    success_url = reverse_lazy("shopapp:products_list")


class ProductUpdateView(UpdateView):
    template_name = "shopapp/product-update.html"
    fields = "name", "price", "description", "discount"
    model = Product

    def get_success_url(self):
        return reverse(
            "shopapp:product_detail",
            kwargs={"pk": self.object.pk},
        )


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("shopapp:products_list")


class OrdersListView(ListView):
    queryset = Order.objects.select_related("user").prefetch_related("products")
    template_name = "shopapp/orders-list.html"
    context_object_name = "orders"


class OrderDetailView(DetailView):
    template_name = "shopapp/order-detail.html"
    queryset = Order.objects.select_related("user").prefetch_related("products")
    context_object_name = "order"


class OrderCreateView(CreateView):
    template_name = "shopapp/order-create.html"
    queryset = Order.objects.select_related("user").prefetch_related("products")
    fields = "delivery_address", "promocode", "products"
    success_url = reverse_lazy("shopapp:orders_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class OrderUpdateView(UpdateView):
    model = Order
    template_name = "shopapp/order-update.html"
    fields = ("delivery_address", "promocode", "products")

    def get_queryset(self):
        return (
            Order.objects
            .select_related("user")
            .prefetch_related("products")
            .filter(user=self.request.user)
        )

    def get_success_url(self):
        return reverse(
            "shopapp:order_detail",
            kwargs={"pk": self.object.pk},
        )
        

class OrderDeleteView(DeleteView):
    template_name = "shopapp/order_confirm_delete.html"
    queryset = Order.objects.select_related("user").prefetch_related("products")
    success_url = reverse_lazy("shopapp:orders_list")
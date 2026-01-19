from django.urls import path
from .views import (
    shop_index,
    groups_list,
    ProductsListView,
    ProductCreateView,
    ProductDetailView,
    ProductUpdateView,
    ProductDeleteView,
    OrdersListView,
    OrderCreateView,
    OrderDetailView,
    OrderUpdateView,
    OrderDeleteView,
)

app_name = "shopapp"


urlpatterns = [
    path("", shop_index, name="index"),
    path("groups/", groups_list, name="groups_list"),
    path("products/", ProductsListView.as_view(), name="products_list"),
    path("products/create", ProductCreateView.as_view(), name="create_product"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("products/<int:pk>/update", ProductUpdateView.as_view(), name="product_update"),
    path("products/<int:pk>/delete", ProductDeleteView.as_view(), name="product_delete"),
    path("orders/", OrdersListView.as_view(), name="orders_list"),
    path("orders/create", OrderCreateView.as_view(), name="create_order"),
    path("orders/<int:pk>/", OrderDetailView.as_view(), name="order_detail"),
    path("orders/<int:pk>/update", OrderUpdateView.as_view(), name="order_update"),
    path("orders/<int:pk>/delete", OrderDeleteView.as_view(), name="order_delete"),
]

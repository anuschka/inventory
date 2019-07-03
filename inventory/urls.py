from django.urls import path
from inventory import views
from inventory.apiviews import ProductList, ProductDetail, BatchList, BatchDetail
from inventory.apiviews import ExpiredProducts, FreshProducts, ExpiringProducts, OrderList

urlpatterns = [
    # product endpoints
    path("products/", ProductList.as_view(), name="product_list"), 
    path("products/<int:pk>/", ProductDetail.as_view(), name="product_detail"),
    # batch endpoints
    path("batches/", BatchList.as_view(), name="batch_list"), 
    path("batches/<int:pk>/", BatchDetail.as_view(), name="batch_detail"),
    # expired products
    path("expired/", ExpiredProducts.as_view(), name="expired"), 
    # fresh products
    path("fresh/", FreshProducts.as_view(), name="fresh"),
    # expired products
    path("expiring/", ExpiringProducts.as_view(), name="expiring"),
    # order endpoints
    path("orders/", OrderList.as_view(), name="order_list"), 
]




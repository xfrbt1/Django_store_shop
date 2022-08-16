from django.urls import path, include
from django.views.generic import TemplateView
from shop import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='shop'),
    # path('cart_basket_view/', TemplateView.as_view(template_name='shop/cart.html'), name='cart'),
    path('cart_view/', views.cart_view, name='cart'),
    # path('product_detail/<int:pk>', TemplateView.as_view(template_name='shop/shop_detail.html'), name='shop_detail'),
    path('add_item_to_cart/<int:pk>', views.add_item_to_cart, name='add_item_to_cart'),
    path('delete_item/<int:pk>', views.CartDeleteItem.as_view(), name='cart_delete_item'),
<<<<<<< HEAD
=======
    path('make_order', views.make_order, name='make_order'),
>>>>>>> 800faf1 (Initial commit)
]

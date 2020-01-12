from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home , name="home"),
    path('product/<int:pk>/' , views.product_detail , name="product-detail"),
    path('newproduct/' , views.NewProduct , name="new-product"),
    path('mysellership/' , views.cancel_sellership , name='cancel-sellership'),
    path('getsellership/' , views.get_sellership , name="get-sellership"),    
    path('confirmsellership/' , views.confirm_sellership , name="confirm-sellership"),
    path('advisesellership/' , views.get_sellership_advise , name="sellership-advise"),
    path('deposit/' , views.deposit , name="user-deposit"),
    path('successfuldeposit' , views.successful_deposit , name="successful-deposit"),
    path('search/' , views.search_bar , name="search"),
    path('added/<int:pk>/' , views.add_to_cart , name="add-cart"),
    path('cart/' , views.user_cart , name="user-cart"),
    path('cart/delete/<int:pk>/' , views.delete_cart_items , name="delete-cart"),
    path('payment/' , views.proceed_payment , name="proceed-payment"),
    path('payment/successful_payment' , views.successful_payment , name="successful-payment"),
    path('my_products/' , views.my_products , name="my-products"),
    path('seller_orders/' , views.seller_orders , name="seller-orders"),
    path('edit_product/<int:pk>/' , views.edit_product , name="edit-product"),
    path('confirmed_edit/<int:pk>/' , views.confirm_edit , name="confirm-edit"),
    path('delete_product/<int:pk>/' , views.delete_product , name="delete-product"),
    path('order_detail/<int:pk>/' , views.order_detail , name="order-detail"),
    path('tracking_number/<int:pk>' , views.tracking_number , name="tracking-number"),
    path('my_orders/' , views.my_orders , name="my-orders"),
    path('review/<int:pk>/' , views.confirm_review , name="review-confirmation")
]

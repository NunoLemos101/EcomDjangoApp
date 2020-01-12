from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile , CreditCard
from Ecom.models import Product , Order , Review
from crispy_forms.layout import Field

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProductRegisterForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ['title' , 'content' , 'price' , 'shipping_price' , 'shipping_time' , 'stock' , 'image1' , 'image2' , 'image3']
    
class CreditCardRegisterForm(forms.ModelForm):

    class Meta:
        model = CreditCard
        fields = ['CardNumber' , 'CVV' , 'Owner' , 'ValidationYear' , 'ValidationMonth' , 'WithdrawAmount']

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['address_line_1' , 'address_line_2' , 'Country' , 'state' , 'city' , 'ZIP_code']

class OrderUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Order
        fields = ['tracking_number']

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = [ 'title' , 'content' , 'rating' ]
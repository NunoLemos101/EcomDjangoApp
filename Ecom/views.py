from users.forms import ProductRegisterForm , CreditCardRegisterForm , OrderForm , OrderUpdateForm , ReviewForm
from django.shortcuts import render , HttpResponse , HttpResponseRedirect , reverse
from django.contrib import messages
from users.models import User , Profile
from django.contrib.auth.decorators import login_required , permission_required
from datetime import datetime , timedelta
from .models import Product , AddCart , Order , Review
from collections import Counter
import datetime
import random
import re

def home(request):
    products = list(Product.objects.filter(show=True))
    random_number_1 = random.randint(0 , len(products) - 1)
    product_1 = products[random_number_1]
    products.pop(random_number_1)
    random_number_2 = random.randint(0 , len(products) - 1)
    product_2 = products[random_number_2]
    products.pop(random_number_2)
    random_number_3 = random.randint(0 , len(products) - 1)
    product_3 = products[random_number_3]
    products.pop(random_number_3)
    random_number_4 = random.randint(0 , len(products) - 1)
    product_4 = products[random_number_4]
    products.pop(random_number_4)
    random_products = []

    random_products.append(product_1)
    random_products.append(product_2)
    random_products.append(product_3)
    random_products.append(product_4)
    stuff_for_frontend = {
        'random_products': random_products,
    }
    return render(request , 'ecom/home.html' , stuff_for_frontend)

def product_detail(request , pk):
    
    selected_product = Product.objects.get(pk=pk)
    selected_product.clicks_count = selected_product.clicks.count()
    selected_product.save()

    search_text = selected_product.title
    search_text_list = re.sub("[^\w]", " ",  search_text).split()
    all_products = Product.objects.all()
    similar_products = []

    for x in search_text_list:
        if Product.objects.filter(show=True , title__contains=x).order_by('clicks_count'):
            for y in list(Product.objects.filter(show=True , title__contains=x)):
                similar_products.append(y.pk)

    similar_products = list( dict.fromkeys(similar_products))
    final_list = []
    
    for z in similar_products:
        product_in_form = Product.objects.get(pk=z , show=True)
        final_list.append(product_in_form)

    final_list_2 = []
    if len(final_list) > 4:
        for i in range(4):
            product = final_list[i]
            final_list_2.append(product)
        
    if len(final_list_2) < 4:
        user_products = list(Product.objects.filter(seller=Product.objects.get(pk=pk).seller , show=True))
        for y in user_products:
            final_list_2.append(y)
    
    final_list_2 = list( dict.fromkeys(final_list_2))

    for y in final_list_2:
        if y.id == Product.objects.get(pk=pk).id:
            final_list_2.remove(y)
    
    if len(final_list_2) < 4:
        while len(final_list_2) <4:
            list_of_all = list(Product.objects.all())
            p = Product.objects.all()[random.randint(1 , len(list_of_all)) - 1]
            final_list_2.append(p)
                       
    if selected_product.show == True:
        if request.user.id:
            if selected_product.clicks.filter(id=request.user.id).exists():
                pass
            else:
                selected_product.clicks.add(request.user)
        else:
            pass

        image_list = []
        
        if selected_product.image2:
            image_list.append(selected_product.image2)
        else:
            pass
        if selected_product.image3:
            image_list.append(selected_product.image3)
        else:
            pass
        numbers = '0123456789'
        ship_time = selected_product.shipping_time

        for searching_number in ship_time:
            if searching_number in numbers:
                days = searching_number
        days = int(days)

        reviews = Review.objects.filter(item=selected_product)
        reviews_count = Review.objects.filter(item=selected_product).count()
        all_ratings = []
        if reviews.count() > 0:
            for review in reviews:
                all_ratings.append(float(review.rating))
            
            sum_of_all_ratings = sum(all_ratings)
            average = sum_of_all_ratings / len(all_ratings)
            average = int(round(average , 0))
        else:
            average = 0

        date_predicted = datetime.datetime.now() + timedelta(days=days)
        content_len = len(selected_product.content)
        form = ReviewForm()
        
        stuff_for_frontend = {
            'average':average,
            'final_list_2':final_list_2,
            'form':form,
            'reviews':reviews,
            'reviews_count':reviews_count,
            'content_len':content_len,
            'date_predicted':date_predicted,
            'selected_product':selected_product,
            'image_list':image_list,
        }
        return render(request , 'ecom/product_detail.html' , stuff_for_frontend)
    else:
        return render(request , 'ecom/noshow.html')

def search_bar(request):
    search_text = request.POST['search_text']
    search_text_list = re.sub("[^\w]", " ",  search_text).split()
    all_products = list(Product.objects.filter(show=True))
    selected_products = []

    for x in search_text_list:
        if Product.objects.filter(show=True , title__contains=x):
            for y in list(Product.objects.filter(show=True , title__contains=x).order_by('-clicks_count')):
                selected_products.append(y.pk)
    
    selected_products = list( dict.fromkeys(selected_products))
    final_list = []
    
    for z in selected_products:
        product_in_form = Product.objects.get(pk=z)
        final_list.append(product_in_form)
        
    

    stuff_for_frontend = {
        'final_list':final_list
    }
    return render(request , 'ecom/search.html' , stuff_for_frontend)

@login_required
def NewProduct(request):
    form = ProductRegisterForm()
    seller = User.objects.get(pk=request.user.id)

    if seller.profile.is_seller == True:
            if request.method == "POST":
                form = ProductRegisterForm(request.POST , request.FILES)
                if form.is_valid():
                    form.instance.seller = request.user
                    form.instance.show = True
                    form.save()
                    
                    return HttpResponseRedirect(reverse('my-products'))
        
    else:
        return render(request , 'ecom/warning_sellership.html')
    
    stuff_for_frontend = {
        'form':form,
    }
    return render(request , 'ecom/product_form.html' , stuff_for_frontend)

@login_required
def cancel_sellership(request):
    if request.user.profile.is_seller == True:
        return render(request , 'ecom/cancel_sellership.html')
    else:
        return render(request , 'ecom/warning_sellership.html')

@login_required
def get_sellership(request):
    if request.user.profile.is_seller == False:
        return render(request , 'ecom/get_sellership.html')
    else:
        return render(request , 'ecom/cancel_sellership.html')

@login_required
def confirm_sellership(request):
    if request.user.profile.is_seller == False:
        return render(request , 'ecom/confirm_sellership.html')
    else:
        return render(request , 'ecom/home.html')

@login_required
def get_sellership_advise(request):
    if request.method == "POST":
        if request.user.profile.money >= 10:
            if request.user.profile.is_seller == False:
                DjangoWallet = User.objects.get(pk=18)                
                request.user.profile.money = request.user.profile.money - 10
                DjangoWallet.profile.money = DjangoWallet.profile.money + 10
                DjangoWallet.profile.save()
                request.user.profile.is_seller = True 
                request.user.profile.money
                request.user.profile.save()
                return render(request , 'ecom/successful_sellership.html')
        else:
            return render(request , 'ecom/no_money.html')   
    else:
        return render(request , 'ecom/home.html')

@login_required
def deposit(request):
    credit_card_form = CreditCardRegisterForm()
    stuff_for_frontend = {
        'cd_form' : credit_card_form,
    }
    return render(request , 'ecom/deposit.html' , stuff_for_frontend)

@login_required
def successful_deposit(request):
    if request.method == "POST":
        if request.user:
            form = CreditCardRegisterForm(request.POST)
            if form.is_valid:
                if request.user.profile:
                    user = request.user
                    form.instance.CardUser = user
                    form.save()
                    if datetime.datetime.now() < datetime.datetime.now().replace(form.instance.ValidationYear , form.instance.ValidationMonth , 1):
                        if form.is_valid:
                            value_being_deposited = form.instance.WithdrawAmount
                            user.profile.money = user.profile.money + value_being_deposited
                            request.user.profile.save()
                            return HttpResponseRedirect(reverse('home'))
        
                    
                    elif datetime.datetime.now() >= datetime.datetime.now().replace(form.instance.ValidationYear , form.instance.ValidationMonth , 1):
                        form.instance.delete()
                        return HttpResponseRedirect(reverse('user-deposit'))
    else:
        return render(request , 'ecom/deposit.html')

@login_required
def add_to_cart(request , pk):
    user = User.objects.get(pk=request.user.id)
    product = Product.objects.get(pk=pk , show=True)
    if request.user != product.seller:
        added_to_cart = AddCart.objects.create(buyer=user , item=product , show=True)
        return HttpResponseRedirect(reverse('user-cart'))
    else:
        return HttpResponseRedirect(reverse('home'))

@login_required
def user_cart(request):
    user = request.user
    products_in_pk = []
    objects_added_to_cart = list(AddCart.objects.filter(buyer=user , show=True))
    for objects in objects_added_to_cart:
        products_in_pk.append(objects.item.id)                                                                                      
    dict_repeat = dict(Counter(products_in_pk))
    
    for x in dict_repeat:
        if dict_repeat[x] != 1:
            product_in_real_form = Product.objects.get(pk=x , show=True)
            number_list = []                                                                                # z=0
            for z in range(AddCart.objects.filter(buyer=request.user , item=product_in_real_form , show=True).count()): #while z < AddCart.objects.filter(buyer=request.user , item=product_in_real_form).count():
                number_list.append(AddCart.objects.filter(buyer=request.user , item=product_in_real_form , show=True)[0].number)         #GENIUS!
                AddCart.objects.filter(buyer=request.user , item=product_in_real_form , show=True)[0].delete()
            sum_of_all = sum(number_list)

            AddCart.objects.create(buyer=request.user , item=product_in_real_form , number = sum_of_all , show=True)

    objects_added_to_cart = AddCart.objects.filter(buyer=user , show=True).order_by('-number')

    checkout_price = []
    checkout_shipping_price = []

    for ioScript in objects_added_to_cart:
        if ioScript.item.show == False:
            ioScript.show = False
            ioScript.save()
        elif ioScript.number > ioScript.item.stock:
            ioScript.show = False
            ioScript.save() 
        else:
            x = ioScript.item.price
            y = ioScript.number
            k = ioScript.item.shipping_price
            z = x * y
            checkout_shipping_price.append(k)
            checkout_price.append(z)


    checkout_price = sum(checkout_price)
    checkout_shipping_price = sum(checkout_shipping_price)
    

    stuff_for_frontend = {
        'checkout_shipping_price':checkout_shipping_price,
        'checkout_price':checkout_price,
        'objects_added_to_cart':objects_added_to_cart,
    }
    return render(request , 'ecom/user_cart.html' , stuff_for_frontend)

def delete_cart_items(request , pk):
    selected_product = AddCart.objects.get(pk=pk)
    selected_product.show = False
    selected_product.save()
    return HttpResponseRedirect(reverse('user-cart'))

@login_required
def proceed_payment(request):
    user = request.user
    products_in_pk = []
    objects_added_to_cart = list(AddCart.objects.filter(buyer=user , show=True))
    for objects in objects_added_to_cart:
        products_in_pk.append(objects.item.id)                                                                                      
    dict_repeat = dict(Counter(products_in_pk))
    
    for x in dict_repeat:
        if dict_repeat[x] != 1:
            product_in_real_form = Product.objects.get(pk=x , show=True)
            number_list = []                                                                                
            for z in range(AddCart.objects.filter(buyer=request.user , item=product_in_real_form , show=True).count()): #while z < AddCart.objects.filter(buyer=request.user , item=product_in_real_form).count():
                number_list.append(AddCart.objects.filter(buyer=request.user , item=product_in_real_form , show=True)[0].number)         #GENIUS!
                AddCart.objects.filter(buyer=request.user , item=product_in_real_form , show=True)[0].delete()
            sum_of_all = sum(number_list)

            AddCart.objects.create(buyer=request.user , item=product_in_real_form , number = sum_of_all , show=True)    
    
    
    cart = AddCart.objects.filter(buyer=request.user , show=True).order_by('-number')
    if cart.count() == 0:
        return render(request , 'ecom/no_items.html')
    else:
        pass
    checkout_price = []
    checkout_shipping_price = []
    for ioScript in cart:
        if ioScript.item.show == False:
            ioScript.show = False
            ioScript.save()
        elif ioScript.number > ioScript.item.stock:
            ioScript.show = False
            ioScript.save() 
        else:
            x = ioScript.item.price
            y = ioScript.number
            k = ioScript.item.shipping_price
            z = x * y
            checkout_shipping_price.append(k)
            checkout_price.append(z)

    checkout_price = sum(checkout_price)
    checkout_shipping_price = sum(checkout_shipping_price)
    total = checkout_price + checkout_shipping_price    

    order_form = OrderForm()  

    if checkout_price == 0:
        return render(request , 'ecom/no_items.html')
        

    stuff_for_frontend = {
        'cart':cart,
        'order_form':order_form,
        'total':total,
    }
    return render(request , 'ecom/order_form.html' , stuff_for_frontend)

@login_required
def successful_payment(request):
    user = request.user
    products_in_pk = []
    objects_added_to_cart = list(AddCart.objects.filter(buyer=user , show=True))
    for objects in objects_added_to_cart:
        products_in_pk.append(objects.item.id)                                                                                      
    dict_repeat = dict(Counter(products_in_pk))
    
    for x in dict_repeat:
        if dict_repeat[x] != 1:
            product_in_real_form = Product.objects.get(pk=x , show=True)
            number_list = []                                                                                
            for z in range(AddCart.objects.filter(buyer=request.user , item=product_in_real_form , show=True).count()): #while z < AddCart.objects.filter(buyer=request.user , item=product_in_real_form).count():
                number_list.append(AddCart.objects.filter(buyer=request.user , item=product_in_real_form , show=True)[0].number)         #GENIUS!
                AddCart.objects.filter(buyer=request.user , item=product_in_real_form , show=True)[0].delete()
            sum_of_all = sum(number_list)

            AddCart.objects.create(buyer=request.user , item=product_in_real_form , number = sum_of_all , show=True)    
    
    
    cart = AddCart.objects.filter(buyer=request.user , show=True).order_by('-number')
    if cart.count() == 0:
        return render(request , 'ecom/no_items.html')
    else:
        pass
    checkout_price = []
    checkout_shipping_price = []
    for ioScript in cart:
        if ioScript.item.show == False:
            ioScript.show = False
            ioScript.save()
        elif ioScript.number > ioScript.item.stock:
            ioScript.show = False
            ioScript.save() 
        else:
            x = ioScript.item.price
            y = ioScript.number
            k = ioScript.item.shipping_price
            z = x * y
            checkout_shipping_price.append(k)
            checkout_price.append(z)

    checkout_price = sum(checkout_price)
    checkout_shipping_price = sum(checkout_shipping_price)
    total = checkout_price + checkout_shipping_price    
    
    def random_tracking_number(any_positive_number):
        alfa = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        nums = '0123456789'
        x = 0
        code_list = []
        while x <= any_positive_number:
            x = x + 1
            y = random.randint(1 , 2)
            
            if y == 1:
                z = random.randint(0 , 25)
                g = alfa[z]
                code_list.append(g)
            else:
                z = random.randint(0 , 9)
                g = nums[z]
                code_list.append(g)
        code = '#'
        for u in range(len(code_list)):
            code = code + str(code_list[u])
        return code
    
    if request.method == "POST":
        if request.user.profile.money >= total:
            order_form = OrderForm(request.POST)            
            if order_form.is_valid:
                request.user.profile.money = request.user.profile.money - total
                request.user.profile.save()
                for product in cart:
                    if product.item.stock >= product.number:
                        product.item.stock = product.item.stock - product.number
                        product.item.save()
                    else:
                        refund_product_price = float(product.item.price)
                        refund_shipping_price = float(product.item.shipping_price)
                        quantity = float(product.number)
                        refund = (refund_product_price * quantity) + refund_shipping_price
                        request.user.profile.money = request.user.profile.money + refund
                        request.user.profile.save() 
                    order_form = OrderForm(request.POST)
                    order_form.instance.buyer = request.user
                    order_form.instance.seller = product.item.seller
                    order_form.instance.ordered_items = product
                    order_form.instance.order_number = random_tracking_number(9)
                    while Order.objects.filter(order_number__contains=order_form.instance.order_number):
                        order_form.instance.order_number = random_tracking_number(9)
                    price = float(product.item.price)
                    shipping_price = float(product.item.shipping_price)
                    quantity = float(product.number)
                    full_price = price * quantity
                    full_price = full_price + shipping_price
                    django_gets = full_price * 0.02
                    django_gets = round(django_gets , 2)
                    seller_gets = full_price - django_gets
                    seller_gets = round(seller_gets , 2)
                    django_wallet = User.objects.get(pk=18)
                    django_wallet_money = float(django_wallet.profile.money)
                    django_wallet.profile.money = django_wallet_money + django_gets
                    seller_money = float(product.item.seller.profile.seller_money)
                    product.item.seller.profile.seller_money = seller_money + seller_gets
                    django_wallet.save()
                    product.item.seller.profile.save()
                    full_price = round(full_price , 2)
                    order_form.instance.price_seller_received = seller_gets
                    order_form.instance.price_paid = full_price
                    order_form.save()
                    product.show = False
                    product.save()
                    
                return render(request , 'ecom/order_placed.html')    
            else:
                return HttpResponseRedirect(reverse('user-cart'))
        else:
            return render(request , 'ecom/no_money.html')

@login_required
def my_products(request):
    if request.user.profile.is_seller == True:
        orders_count = Order.objects.filter(seller=request.user , viewed=False).count()
        user_products = Product.objects.filter(seller=request.user , show=True)
        stuff_for_frontend = {
            'orders_count':orders_count,
            'user_products':user_products,
        }
        return render(request , 'ecom/user_products.html' , stuff_for_frontend)
    else:
        return HttpResponseRedirect(reverse('get-sellership'))
@login_required
def seller_orders(request):
    if request.user.profile.is_seller == True:
        orders = Order.objects.filter(seller=request.user).order_by('-date_placed')
        for order in orders:
            order.viewed = True
            order.save()
        form = OrderUpdateForm()
        stuff_for_frontend = {
            'orders':orders,
            'form':form,
        }
        return render(request , 'ecom/seller_orders.html' , stuff_for_frontend)
    else:
        return HttpResponseRedirect(reverse('get-sellership'))

@login_required
def edit_product(request , pk):
    if request.user.profile.is_seller == True:
        selected_product = Product.objects.get(pk=pk)
        if request.user == selected_product.seller:
            form = ProductRegisterForm(instance=selected_product)
            stuff_for_frontend = {
                'product':selected_product,
                'form':form,
            }
            return render(request , 'ecom/product_edit_form.html' , stuff_for_frontend)
    else:
        return HttpResponseRedirect(reverse('get-sellership'))
@login_required
def confirm_edit(request , pk):
    selected_product = Product.objects.get(pk=pk)
    user = request.user
    if request.method == "POST":
        if user.profile.is_seller == True:
            if selected_product.seller == request.user:
                form = ProductRegisterForm(request.POST , request.FILES , instance=selected_product)
                if form.is_valid():
                    form.instance.seller = request.user
                    form.instance.show = True
                    form.save()
                    return HttpResponseRedirect(selected_product.get_absolute_url())
                else:
                    return HttpResponseRedirect(reverse('edit-product'))
        else:
            return HttpResponseRedirect(reverse('get-sellership'))
@login_required
def delete_product(request , pk):
    selected_product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        if request.user.profile.is_seller == True:
            if request.user == selected_product.seller:
                selected_product.show = False
                selected_product.save()
                return HttpResponseRedirect(reverse('user-cart'))

@login_required    
def order_detail(request , pk):
    order = Order.objects.get(pk=pk)
    if request.user == order.ordered_items.buyer or request.user == order.ordered_items.item.seller:
        stuff_for_frontend = {
            'order':order,
        }
        return render(request , 'ecom/order_detail.html' , stuff_for_frontend)
    else:
        return HttpResponseRedirect(reverse('home'))

@login_required
def tracking_number(request , pk):
    order = Order.objects.get(pk=pk)
    if request.user == order.seller:
        order_form = OrderUpdateForm(request.POST , instance=order)
        if order.first_track_code == False:
            if order_form.is_valid():
                order_form.instance.order_status = 'Order Dispatched'
                order_form.save()
                return HttpResponseRedirect(reverse('seller-orders'))
        elif order.first_track_code == True:
            if order_form.is_valid():
                money_seller_money = order.seller.profile.seller_money
                money_loosing = float(money_seller_money) - float(order.price_seller_received)
                order.seller.profile.seller_money = money_loosing
                order.seller.profile.save()
                money_seller_on_main_account = order.seller.profile.money
                money_winning = float(money_seller_on_main_account) + float(order.price_seller_received)
                order.seller.profile.money = money_winning
                order_form.instance.first_track_code = False
                order.seller.profile.save()
                order_form.instance.order_status = 'Order Dispatched'
                order_form.save()
                return HttpResponseRedirect(reverse('seller-orders'))

@login_required
def my_orders(request):
    user = request.user
    orders = Order.objects.filter(buyer=user).order_by('-date_placed')
    stuff_for_frontend = {
        'orders':orders
    }
    return render(request , 'ecom/my_orders.html' , stuff_for_frontend)

@login_required
def confirm_review(request , pk):
    product = Product.objects.get(pk=pk)
    form = ReviewForm()
    if product.show == True:
        if request.user.id != Product.objects.get(pk=pk).seller.id:
            if Review.objects.filter(customer=request.user , item=Product.objects.get(pk=pk)).count() < 2:
                if form.is_valid:
                    form = ReviewForm(request.POST)
                    form.instance.customer = request.user
                    form.instance.item = product
                    form.save()
                    return HttpResponseRedirect(product.get_absolute_url())
            else:
                messages.error(request , 'You only can Rate 2 times each Product')
                return HttpResponseRedirect(product.get_absolute_url())
        elif request.user.id == Product.objects.get(pk=pk).seller.id:
            messages.error(request , 'You cant rate your own products')
            return HttpResponseRedirect(product.get_absolute_url())
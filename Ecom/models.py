from django.shortcuts import reverse
from django.db import models
from users.models import User , Profile
from django.core.validators import MinValueValidator , MaxValueValidator
from PIL import Image
from django.dispatch import receiver
from django.utils import timezone

class Product(models.Model):
    one_day = '1 Day'
    two_days = '2 Days'
    three_days = '3 Days'
    four_days = '4 Days'
    five_days = '5 Days'
    six_days = '6 Days'
    seven_days = '7 Days'
    SHIPMENT_TIME_CHOICE = [
        (one_day ,'1 Day'),
        (two_days , '2 Days'),
        (three_days , '3 Days'),
        (four_days , '4 Days'),
        (five_days , '5 Days'),
        (six_days , '6 Days'),
        (seven_days , '7 Days'),
    ]
    
    title = models.CharField(max_length=100)    
    content = models.TextField()    
    seller = models.ForeignKey(User , on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8 , decimal_places=2 , validators=[MinValueValidator(0.5)] , default=0)    
    shipping_price = models.DecimalField(max_digits=8 , decimal_places=2 , validators=[MinValueValidator(-0.00)] , default=0)
    shipping_time = models.CharField(choices=SHIPMENT_TIME_CHOICE , max_length=7 , blank=False , default=seven_days)
    stock = models.IntegerField(default=1 , blank=False)
    clicks_count = models.IntegerField(default = 0)
    clicks = models.ManyToManyField(User , related_name="clicks" , blank=True)
    show = models.BooleanField(default=True)
    image1 = models.ImageField(blank=False , default='3i1415926543PI.jpg' , upload_to='images')
    image2 = models.ImageField(default=None , blank=True , upload_to='images')
    image3 = models.ImageField(default=None , blank=True , upload_to='images')

    def save(self , *args , **kwargs):
        super(Product, self).save(*args , **kwargs)

        img1 = Image.open(self.image1.path)
        if self.image2:
            img2 = Image.open(self.image2.path)
            img2.save(self.image2.path)
        else:
            pass
        if self.image3:
            img3 = Image.open(self.image3.path)
            img3.save(self.image3.path)
    
    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        if self.show == False:
            return self.title + " --> Closed"
        elif self.show == True:
            return self.title

class AddCart(models.Model):
    buyer = models.ForeignKey(User , on_delete=models.CASCADE)
    item = models.ForeignKey(Product , on_delete=models.CASCADE)
    number = models.IntegerField(default=1 , validators=[MinValueValidator(1)])
    show = models.BooleanField(default=True)

    def true_price(self):
        price = self.item.price
        quantity = self.number
        return price * quantity

    def true_price_plus_shipping_price(self):
        price = self.item.price
        shipping_price = self.item.shipping_price
        quantity = self.number
        return (price * quantity) + shipping_price


    def __str__(self):
        return "{} added {} to cart".format(self.buyer , self.item)

class Review(models.Model):
    zero_stars = 0
    one_star = 1
    two_stars = 2
    three_stars = 3
    four_stars = 4
    five_stars = 5

    STAR_RATING_CHOICE = [
        (zero_stars , 0 ),
        (one_star , 1),
        (two_stars , 2),
        (three_stars , 3),
        (four_stars , 4),
        (five_stars , 5),
    ]
    
    customer = models.ForeignKey(User , on_delete=models.CASCADE)
    item = models.ForeignKey(Product , on_delete=models.CASCADE)
    title = models.CharField(max_length=100 , default="Title of your Review")
    content = models.TextField(max_length=800 , blank=False , default='What do you think about this product?')
    date_reviewed = models.DateTimeField(default=timezone.now)
    rating = models.IntegerField( choices=STAR_RATING_CHOICE , blank = False , validators=[MinValueValidator(-0.00) , MaxValueValidator(5)])
    show = models.BooleanField(default=True)

    def __str__(self):
        return '{} reviewed {}'.format(self.customer , self.item)

class Order(models.Model):
    order_dispatched = 'Order dispatched'
    not_shipped = 'Not shipped'

    ORDER_STATUS_CHOICE = [
        (not_shipped , 'Not shipped'),
        (order_dispatched , 'Order dispatched'),
    ]

    order_status = models.CharField(choices=ORDER_STATUS_CHOICE , default=not_shipped , max_length=100)
    first_track_code = models.BooleanField(default=True)
    order_number = models.CharField(max_length=20 , blank=False , default="Error")
    tracking_number = models.CharField(max_length=200 , blank=True , default="Not Provided Yet")
    ordered_items = models.ForeignKey(AddCart , on_delete=models.CASCADE)
    buyer = models.ForeignKey(User , related_name="buyer" , on_delete=models.CASCADE)    
    seller = models.ForeignKey(User , related_name="seller" , on_delete = models.CASCADE)
    address_line_1 = models.CharField(max_length=100 , blank=False)
    address_line_2 = models.CharField(max_length=100 , blank=True)
    Country = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    ZIP_code = models.CharField(max_length=20)
    viewed = models.BooleanField(default=False)
    date_placed = models.DateTimeField(default=timezone.now)
    price_paid = models.DecimalField(max_digits=8 , decimal_places=2 , validators=[MinValueValidator] , blank=False , default=0.10)
    price_seller_received = models.DecimalField(max_digits=8 , decimal_places=2 , validators=[MinValueValidator(-0.00)] , blank=False , default=0.10 )

    def __str__(self):
        return '{} ordered {}'.format(self.buyer , self.ordered_items.item)
    

    
    
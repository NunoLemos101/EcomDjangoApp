from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import  MinValueValidator , MaxValueValidator
from PIL import Image
import datetime

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    image = models.ImageField(default="3i1415926543PI.jpg" , upload_to="images")
    seller_money = models.DecimalField(max_digits=8 , decimal_places=2 , validators=[MinValueValidator(-0.00)] , default=0)
    money = models.DecimalField(max_digits=8 , decimal_places=2 , validators=[MinValueValidator(-0.00)] , default=0)
    is_seller = models.BooleanField(default=False)

    def save(self , *args , **kwargs):
        super(Profile, self).save(*args , **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300 , 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return f'{self.user.username} Profile'
    
class CreditCard(models.Model):
    
    YEAR_CHOICE = [(y , y) for y in range(2019 , datetime.date.today().year + 8)]
    MONTH_CHOICE = [(m,m) for m in range(1,13)]

    CardUser = models.ForeignKey(User , on_delete=models.CASCADE)
    CardNumber = models.IntegerField(blank=False , validators=[MaxValueValidator(9999999999999999)])
    CVV = models.IntegerField(blank=False , validators=[MaxValueValidator(9999)])
    Owner = models.CharField(blank=False , max_length=25)
    ValidationYear = models.IntegerField(blank=False , choices=YEAR_CHOICE)
    ValidationMonth = models.IntegerField(blank=False , choices=MONTH_CHOICE)
    WithdrawAmount = models.DecimalField(max_digits=8 , decimal_places=2 , validators=[MinValueValidator(-0.00)] , default=0)

    def __str__(self):
        return "Deposit number #{}".format(self.pk)
    
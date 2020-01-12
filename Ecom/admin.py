from django.contrib import admin
from .models import Product , AddCart , Review , Order

admin.site.register(Product)
admin.site.register(AddCart)
admin.site.register(Review)
admin.site.register(Order)

# Register your models here.

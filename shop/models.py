from django.db import models
from djmoney.models.fields import MoneyField
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
#10admin
#tenten123

class Product (models.Model):
    name=models.CharField(max_length=20,null=False)
    quantity=models.PositiveIntegerField(null=False)
    pricePerKg=MoneyField(max_digits=7,decimal_places=2,default_currency=' AED')
    itemImage=models.ImageField(blank=True,upload_to='ShopItems')
    lastUpdated = models.DateTimeField(auto_now=True, auto_now_add=False)
    addedOn = models.DateTimeField(default=timezone.now())
    addedBy = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

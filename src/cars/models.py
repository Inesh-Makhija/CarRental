from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Car(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1,
    on_delete=models.CASCADE)
    # stripe_price_id = 
    name = models.CharField(max_length=120)
    handle = models.SlugField(unique=True) #slug
    price = models.IntegerField(default=None)
    og_price = models.IntegerField(default=None)
    # stripe_price_id = 
    stripe_price = models.IntegerField(default=None) 
    price_changed_timestamp = models.DateTimeField(auto_now=False, auto_now_add=False,
    blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.price != self.og_price:
            # price changed
            self.og_price = self.price
            # trigger and API request fro the price
            self.stripe_price = self.price
            self.price_changed_timestamp = timezone.now()
        super().save(*args, **kwargs)
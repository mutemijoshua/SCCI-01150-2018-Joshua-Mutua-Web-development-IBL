from django.db import models
from authentication.models import User

# Create your models here.
class buyshares(models.Model):
    amount = models.DecimalField(max_length=50,max_digits=255,decimal_places=2)
    owner = models.ForeignKey(to=User,on_delete=models.CASCADE)
    Datepurchased = models.DateTimeField(auto_now=True)
    Dateupdated = models.DateTimeField(auto_now_add=True)

    
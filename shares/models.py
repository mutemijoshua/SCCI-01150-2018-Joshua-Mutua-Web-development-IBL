from django.db import models
from authentication.models import User

class shares(models.Model):
    owner = models.ForeignKey(to=User,on_delete=models.CASCADE)
    number_of_shares = models.DecimalField
    Date_purchased = models.DateTimeField(auto_now=True)
    Date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return str(self.owner)+'s shares'

# Create your models here.

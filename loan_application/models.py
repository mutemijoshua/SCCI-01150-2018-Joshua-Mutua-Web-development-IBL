from django.db import models
from authentication.models import User
from django.utils import timezone
# Create your models here.
class loanapplication(models.Model):
    amountb= models.DecimalField(max_length=50,max_digits=255,decimal_places=2)
    owner = models.ForeignKey(to=User,on_delete=models.CASCADE)
    Dateborrowed = models.DateTimeField(default = timezone.now)
def __str__(self):
        
        return self.owner

    
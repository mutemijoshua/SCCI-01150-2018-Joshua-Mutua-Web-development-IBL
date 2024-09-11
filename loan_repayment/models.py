from django.db import models
from authentication.models import User
from django.utils import timezone
# Create your models here.
class loanrepayment(models.Model):
    amountp = models.DecimalField(max_length=50,max_digits=255,decimal_places=2,default= 0)
    owner = models.ForeignKey(to=User,on_delete=models.CASCADE)
    Daterepayed = models.DateTimeField(auto_now=True)

def __str__(self):
        
        return self.owner
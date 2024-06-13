from django.db import models
from authentication.models import User
from helpers.models import TrackingModel
class loans(models.Model):
    status_options = [
        ('active','active'),
        ('inactive','inactive')
    ]
    amount_borrowed=models.DecimalField(max_length=50 ,max_digits=255,decimal_places=2)
    loan_balance=models.DecimalField(max_length=50,max_digits=255,decimal_places=2)
    date_borrowed= models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    due_Date= models.DateTimeField(blank=False)
    owner= models.ForeignKey(to=User,on_delete=models.CASCADE)
    loan_status=models.CharField(choices=status_options,max_length=255)

    def __str__(self) :
        return str(self.owner)+'s expenses'
    
    # Create your models here.

from django.shortcuts import render
from .models import buyshares
from shares.models import shares
# Create your views here.
from loan_repayment.models import loanrepayment
from django_daraja.mpesa.core import MpesaClient
from django.http import HttpResponse
from authentication.models import User

# Create your views here.
def Buy_shares(request):
    user = User()
    if request.method == 'POST':
        context ={'data' : request.POST}
        amount = request.POST.get('amount')
        cl = MpesaClient()

        phone_number = user.phonenumber
        amount = 1
        transaction_desc = 'Description'
        occassion = 'Occassion'
        callback_url = 'https://api.darajambili.com/b2c/result'
        response = cl.business_payment(phone_number, amount, transaction_desc, callback_url, occassion)
        
        bshares = buyshares()
        bshares.amount = amount
        bshares.owner = request.user
        bshares.save()

        Shares = shares()
        Shares.number_of_shares = amount * 10
        Shares.owner = request.user
        Shares.save()
        return HttpResponse(response)
    return render(request, 'loan_application/loan_application.html')

# Create your views here.

from django.shortcuts import render,redirect
from .models import loanrepayment
from django.shortcuts import get_object_or_404
from loans.models import loans
from django.http import HttpResponse
from django.urls import reverse
from django_daraja.mpesa.core import MpesaClient

# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required
def Loanrepayment(request, id):
    
    L = get_object_or_404(loans, pk=id)
    context = {'L': L }
    amount = 0
    if request.method == 'POST': 
       
        
        amount_entered = request.POST.get('amount')
        cl = MpesaClient()
        phone_number = request.POST.get('phonenumber')
        amount = int(amount_entered)
        account_reference = 'reference'
        transaction_desc = 'Description'
        callback_url = 'https://api.darajambili.com/express-payment'
        response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
       
        lrepayment= loanrepayment()

        lrepayment.amountp = amount
        lrepayment.owner = request.user
        lrepayment.save()
        bal = L.loan_balance 
        L.loan_balance=int(bal) - int(amount)
        L.save()
        HttpResponse(response)
        return redirect('home')

    return render(request, 'loan_repayment/loan_repayment.html',context)

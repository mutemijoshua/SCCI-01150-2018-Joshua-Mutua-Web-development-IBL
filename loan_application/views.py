from django.shortcuts import render,redirect
from .models import loanapplication
from loans.models import loans
from loan_repayment.models import loanrepayment
from django_daraja.mpesa.core import MpesaClient
from django.http import HttpResponse
from authentication.models import User
# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required
def Loanaplication(request):
    user = User()
    if request.method == 'POST':
        context ={'data' : request.POST}
        amount = request.POST.get('amount')
    
        lapplication= loanapplication()
        loan = loans()

        lapplication.amountb = amount
        lapplication.owner = request.user
        lapplication.save()
        loan.amount_borrowed = amount
        loan.loan_balance = loan.amount_borrowed
        if loan.loan_balance >= 0 :
            loan.loan_status = 'active'
        else:
            loan.loan_status = 'inactive'

        loan.owner = request.user
        loan.save()
        return redirect('home')
    return render(request, 'loan_application/loan_application.html')

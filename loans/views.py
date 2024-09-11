from django.shortcuts import render
from .models import loans
from shares.models import shares
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def Loans(request):
    q = request.GET.get(None)
    if q is None :
        L= loans.objects.all()
    return render(request,'index.html', {'L': L})
def Loan_detail(request, id): 
    L = get_object_or_404(loans, pk=id)
    context = {'L': L }
    return render(request,'loans/loans_detail.html',context)

    

    






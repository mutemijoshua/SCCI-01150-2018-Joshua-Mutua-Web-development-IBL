
from django.contrib import admin
from django.urls import path,include
from loans.views import Loans
from authentication.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Loans, name='home'),
    path('authentication/',include('authentication.urls')),
    path('loans/',include('loans.urls')),
    path('buyshares/',include('buyshares.urls')),
    path('application/',include('loan_application.urls')),
    path('loanrepayment/',include('loan_repayment.urls'))
]

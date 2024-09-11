from django.urls import path

from . import views

urlpatterns = [
    path('loandetail/<id>/',views.Loan_detail, name='loandetail')
]
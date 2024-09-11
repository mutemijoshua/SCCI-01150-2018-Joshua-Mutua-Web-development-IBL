from django.urls import path

from . import views

urlpatterns = [
    path('loanrepayment/<id>/',views.Loanrepayment, name='loanrepayment')
]
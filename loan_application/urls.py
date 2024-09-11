from django.urls import path

from . import views

urlpatterns = [
    path('loanapplication',views.Loanaplication, name='loanapplication')
]
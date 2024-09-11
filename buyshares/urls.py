from django.urls import path

from . import views

urlpatterns = [
    path('',views.Buy_shares, name='buyshares')
]
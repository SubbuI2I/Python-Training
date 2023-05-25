#django
from django.urls import path

#application 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('payment/', views.payment, name='payment'),
    path('payment-done/', views.payment_done, name='payment-done'),
    path('payment-cancelled/', views.payment_cancelled, name='payment-cancelled'),
]
from . import views
from django.urls import path


urlpatterns = [
    path('',views.get_plaid_accounts, name='plaid-accounts'),
    path('handshake/',views.plaid_handshake, name='plaid-handshake')    
]
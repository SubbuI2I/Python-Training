from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from plaid.api import plaid_api
import plaid
# plaid application imports
from banking_api.settings import env

# Create your views here.
plaid_client_id = env('PLAID_CLIENT_ID')
plaid_secret = env('PLAID_SECRET')
plaid_env = env('PLAID_ENV')
configuration = plaid.Configuration(
        host = plaid_env,
        api_key = {
            'clientId': plaid_client_id,
            'secret': plaid_secret
        }
    )
api_client =  plaid.ApiClient(configuration)
client = plaid_api.PlaidApi(api_client) 

@csrf_exempt
def plaid_handshake(request):
    # Create a Plaid client object
    if request.method == 'POST':
        # Exchange public token for access token
        response = client.item_create_public_token.exchange(request.POST.get('public_token'))

        # Return the access token
        return HttpResponse(response['access_token'])
    else:
        context = {
            'plaid_client_id': env('PLAID_CLIENT_ID'),
            'plaid_secret' : env('PLAID_SECRET'),
            'plaid_env' : env('PLAID_ENV')
        }
        return render(request, 'plaid_api/plaid_handshake.html', context)

def get_plaid_accounts(request): 
    
    
    context = {
        'plaid_env': plaid_env,
        'plaid_client_id': plaid_client_id,
        'plaid_secret': plaid_secret
    }
    return render(request, 'plaid_api/accounts.html', context)
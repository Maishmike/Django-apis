import json
import requests
from requests.auth import HTTPBasicAuth
from django.shortcuts import render


# Create your views here.


def token(request):
    consumer_key = 'RFaph9yk6FwUgcD9ZIyHavCPnMMklMzY'
    consumer_secret = 'mJIzolfBRjNWuFjF'
    api_url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    response = requests.get(api_url, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    access_token = json.loads(response.text)
    return render(request, 'token.html', {'token': access_token})


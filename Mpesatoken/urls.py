from django.urls import path
from Mpesatoken.views import token

urlpatterns = [
    path('', token, name='token')
]

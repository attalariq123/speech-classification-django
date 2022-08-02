import email
from django.shortcuts import render

from email_network.models import EmailNetwork

def index(request):
    email_network = EmailNetwork.objects.all()
    context = {'email_network': email_network}
    return render(request, 'email_network/index.html', context)
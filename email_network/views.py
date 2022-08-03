import email
from django.shortcuts import render

from email_network.models import Division, EmailNetwork

def index(request):
    email_network = EmailNetwork.objects.all()
    division = Division.objects.all()
    context = {'email_network': email_network, 'division': division}
    return render(request, 'email_network/index.html', context)
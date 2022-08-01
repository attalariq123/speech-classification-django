from message.models import Message
from django.shortcuts import render

def index(request):
    return render(request, 'email_network/index.html')
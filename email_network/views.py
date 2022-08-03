from ast import Div
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from django.urls import reverse
from email_network.models import Department, Division, EmailNetwork

def index(request):
    email_network = EmailNetwork.objects.all()
    division = Division.objects.all()
    context = {'email_network': email_network, 'division': division}
    return render(request, 'email_network/index.html', context)

def create(request):
    users = User.objects.all()
    divisions = Division.objects.all()
    departments = Department.objects.all()
    context = {'users': users, 'divisions': divisions, 'departments': departments}
    return render(request, 'email_network/create.html', context)

def save(request):
    email_network = EmailNetwork.objects.create(
        sender= User.objects.get(id=request.POST['sender']),
        receiver= User.objects.get(id=request.POST['receiver']), 
        posting_division= Division.objects.get(id=request.POST['posting_division']),
        posting_department= Department.objects.get(id=request.POST['posting_department']), 
        comment_division= Division.objects.get(id=request.POST['comment_division']), 
        comment_department= Department.objects.get(id=request.POST['comment_department']), 
        n=request.POST['amount']
        )

    email_network.save()

    return HttpResponseRedirect(reverse('email_network:index'))

def detail(request, id):
    email_network = get_object_or_404(EmailNetwork, id=id)
    context = {'email_network': email_network}

    return render(request, 'email_network/detail.html', context)

def edit(request, id):
    email_network = get_object_or_404(EmailNetwork, id=id)
    users = User.objects.all()
    divisions = Division.objects.all()
    departments = Department.objects.all()
    context = {'email_network': email_network, 'users':users, 'divisions': divisions, 'departments': departments}

    return render(request, 'email_network/edit.html', context)

def update(request, id):
    email_network = get_object_or_404(EmailNetwork, id=id)

    email_network.sender = User.objects.get(id=request.POST['sender'])
    email_network.receiver = User.objects.get(id=request.POST['receiver'])
    email_network.posting_division = Division.objects.get(id=request.POST['posting_division'])
    email_network.posting_department = Department.objects.get(id=request.POST['posting_department'])
    email_network.comment_division = Division.objects.get(id=request.POST['comment_division'])
    email_network.comment_department = Department.objects.get(id=request.POST['comment_department'])
    email_network.n = request.POST['amount']

    email_network.save()

    return HttpResponseRedirect(reverse('email_network:index'))

def delete(request, id):
    email_network = get_object_or_404(EmailNetwork, id=id)
    email_network.delete()

    return HttpResponseRedirect(reverse('email_network:index'))

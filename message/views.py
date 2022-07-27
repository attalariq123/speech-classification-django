from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from message.models import Message

def index(request):
    message_list = Message.objects.all()
    context = {'message': message_list}

    return render(request, 'message/index.html', context)

def add(request):
    return render(request, 'message/add.html')

def detail(request, id):
    message = get_object_or_404(Message, id=id)
    context = {'message': message}

    return render(request, 'message/detail.html', context)

def edit(request, id):
    message = get_object_or_404(Message, id=id)
    context = {'message': message}

    return render(request, 'message/edit.html', context)

def update(request, id):
    message = get_object_or_404(Message, id=request.POST['id'])
    message.username = request.POST['username']
    message.text = request.POST['text']
    message.save()

    return HttpResponseRedirect(reverse('message:index'))

def save(request):
    message = Message.objects.create(username= request.POST['username'], text = request.POST['text'])
    message.save()

    return HttpResponseRedirect(reverse('message:index'))

def delete(request, id):
    message = get_object_or_404(Message, id=id)
    message.delete()

    return HttpResponseRedirect(reverse('message:index'))
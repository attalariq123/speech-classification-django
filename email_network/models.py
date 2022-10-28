from django.contrib.auth.models import User
from django.db import models

class Division(models.Model):
    name = models.CharField(max_length=64)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=64)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Interaction(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class EmailNetwork(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    posting_division = models.ForeignKey(Division, on_delete=models.CASCADE, related_name='posting_division')
    posting_department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='posting_department')
    comment_division = models.ForeignKey(Division, on_delete=models.CASCADE, related_name='comment_division')
    comment_department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='comment_department')
    n = models.IntegerField(null=False)
    interaction = models.ForeignKey(Interaction, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sender.first_name + ' ' + self.sender.last_name + ' to ' + self.receiver.first_name + ' ' + self.receiver.last_name


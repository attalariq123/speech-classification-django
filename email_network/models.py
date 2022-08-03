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


class EmailNetwork(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    posting_division = models.ForeignKey(Division, on_delete=models.CASCADE, related_name='posting_division')
    posting_department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='posting_department')
    comment_division = models.ForeignKey(Division, on_delete=models.CASCADE, related_name='comment_division')
    comment_department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='comment_department')
    n = models.IntegerField(null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sender.first_name + ' ' + self.sender.last_name + ' to ' + self.receiver.first_name + ' ' + self.receiver.last_name






# class Division(models.TextChoices):
    #     Area_Marketing_Division = 'Area Marketing Division'
    #     Audit_Division = 'Audit Division'
    #     Sales_Distribution_Division = 'Sales & Distribution Division'
    #     Finance_Division = 'Finance Division'
    #     Corporate_Communication_Division = 'Corporate Communication Division'
    #     Strategic_Marketing_Division = 'Strategic Marketing Division'
    #     Media_Digital_Business_Division = 'Media & Digital Business Division'
    #     Information_System_Division = 'Information System Division'
    # class Department(models.TextChoices):
    #     CPA = 'CPA'
    #     CPE = 'CPE'
    #     CPB = 'CPB'
    #     CPD = 'CPD'
    #     CPI = 'CPI'
    #     CPF = 'CPF'
    #     CPY = 'CPY'
    #     CPC = 'CPC'
    #     DDG = 'DDG'
    #     DDE = 'DDE'
    #     DDJ = 'DDJ'
    #     MEB = 'MEB'
from django.db import models
class EmailNetwork(models.Model):
    class Division(models.TextChoices):
        Area_Marketing_Division = 'Area Marketing Division'
        Audit_Division = 'Audit Division'
        Sales_Distribution_Division = 'Sales & Distribution Division'
        Finance_Division = 'Finance Division'
        Corporate_Communication_Division = 'Corporate Communication Division'
        Strategic_Marketing_Division = 'Strategic Marketing Division'
        Media_Digital_Business_Division = 'Media & Digital Business Division'
        Information_System_Division = 'Information System Division'
    class Department(models.TextChoices):
        CPA = 'CPA'
        CPE = 'CPE'
        CPB = 'CPB'
        CPD = 'CPD'
        CPI = 'CPI'
        CPF = 'CPF'
        CPY = 'CPY'
        CPC = 'CPC'
        DDG = 'DDG'
        DDE = 'DDE'
        DDJ = 'DDJ'
        MEB = 'MEB'

    sender = models.CharField(max_length=120)
    receiver = models.CharField(max_length=120)
    posting_division = models.CharField(max_length=120, choices=Division.choices)
    posting_department = models.CharField(max_length=120, choices=Department.choices)
    comment_division = models.CharField(max_length=120, choices=Division.choices)
    comment_department = models.CharField(max_length=120, choices=Department.choices)
    n = models.IntegerField(null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sender + " to " + self.receiver
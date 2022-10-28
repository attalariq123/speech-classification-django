from ast import Div
from django.contrib import admin
from .models import EmailNetwork, Division, Department, Interaction

admin.site.register(EmailNetwork)
admin.site.register(Division)
admin.site.register(Department)
admin.site.register(Interaction)

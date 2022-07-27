from django.db import models

class Message(models.Model):
    username = models.CharField(max_length=200)
    text = models.TextField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

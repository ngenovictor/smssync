from django.db import models

# Create your models here.
class Message(models.Model):
    num_from = models.CharField(max_length=500, blank=True)
    message_id = models.CharField(max_length=500, blank=True)
    sent_timestamp = models.CharField(max_length=500, blank=True)
    sent_to = models.CharField(max_length=500, blank=True)
    device_id = models.CharField(max_length=500, blank=True)
    message = models.CharField(max_length=500)

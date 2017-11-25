from django.db import models

# Create your models here.
class Message(models.Model):
    num_from = models.CharField(max_length=500)
    message_id = models.CharField(max_length=500)
    sent_timestamp = models.CharField(max_length=500)
    sent_to = models.CharField(max_length=500)
    device_id = models.CharField(max_length=500)
    message = models.CharField(max_length=500)

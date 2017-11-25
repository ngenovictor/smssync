from django.contrib import admin
from api.models import Message

# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    list_display = ("message",)

admin.site.register(Message, MessageAdmin)

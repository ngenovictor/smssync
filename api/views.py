from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.shortcuts import redirect
from django.conf import settings
import os
from api.serializer import MessageSerializer

# Create your views here.
@csrf_exempt
def sms_details(request):
    if request.method == "POST":
        data = JSONParser().parse(request)

        try:
            secret = data["secret"]
            num_from = data["from"]
            message_id = data["message_id"]
            message = data["message"]
            sent_timestamp = data["sent_timestamp"]
            sent_to = data["sent_to"]
            device_id = data["device_id"]
            success = "true"
        except KeyError as e:
            message = "No key value representing: {0}".format(e)
            print(e)
            secret = ""
            num_from = ""
            message_id = ""
            message = ""
            sent_timestamp = ""
            sent_to = ""
            device_id = ""
            success = "false"

        

        if len(num_from) > 0 and len(message) > 0 and len(sent_timestamp) > 0 and len(sent_to) > 0 and success == "true":
            if secret != "123456":
                success = "false"
            else:
                data = {
                    "num_from":num_from,
                    "message_id":message_id,
                    "sent_timestamp":sent_timestamp,
                    "sent_to":sent_to,
                    "device_id":device_id,
                    "message":message
                }
                serializer = MessageSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()

                # string = "From : %s\n" %(num_from)
                # string += "Message: %s\n" %(message)
                # string += "Timestamp: %s\n" %(sent_timestamp)
                # string += "Message Id: %s\n" %(message_id)
                # string += "Sent to: %s\n\n\n" %(sent_to)


                # writefile = "log.txt"

                # fh = open(os.path.join(settings.MEDIA_ROOT, writefile), 'a')

                # fh.write(string)

                # fh.close()

        else:
            message = "your data was incorrect check if you are missing a parameter"
            success = "false"


        reply = {"payload":{"success": success},"message":message}
        
        return JsonResponse(reply)

def home(request):
    reply = {
        "message":"the app works. push your info to /sms as a post request in raw json format",
        "sample json ruquest":str({
                "secret":"123456",
                "from":"+254720123456",
                "message_id":1,
                "message":"hey this is a message",
                "sent_timestamp":"12-12-12",
                "sent_to":"+254736736736",
                "device_id":12
            })
    }

    return JsonResponse(reply)   

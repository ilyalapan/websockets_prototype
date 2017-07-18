from channels import Group
import json
from example.models import Requests

def ws_connect(message):
    Group('users').add(message.reply_channel)

def ws_disconnect(message):
    Group('users').discard(message.reply_channel)

def ws_message(message):
    content = json.loads(message.content['text'])
    request_id = content['request_id']
    request = Requests.objects.get(id=request_id)
    if content['status'] == 'success':
        request.status = True
        request.save()



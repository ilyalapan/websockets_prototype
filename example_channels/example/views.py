from django.shortcuts import render
from channels import Group
from example.models import Requests
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from channels.asgi import get_channel_layer



import json

@require_http_methods(["POST"])
def user_list(request):
    return render(request, 'example/user_list.html')

@require_http_methods(["POST"])
@csrf_exempt
def open_box(request):
    box_number = request.POST.get('box_number')
    if not box_number:
        return JsonResponse({'error' : 'Box number not set'})
    r = Requests()
    channel_layer = get_channel_layer()
    ch_group_list = channel_layer.group_channels('users')
    print('List of connected users: ',ch_group_list)
    r.status = True if len(ch_group_list) else False
    r.save()
    Group('users').send({
        'text': json.dumps({'request' : dict(r), 
            'box_number' : box_number,
            })
    })
    return JsonResponse(dict(r))

@require_http_methods(["POST"])
def check_status(request):
    request_id = request.POST.get('request_id')
    request = Requests.objects.get(id=request_id)
    return JsonResponse(dict(r))



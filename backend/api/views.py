import json

from django.shortcuts import render
from django.http import JsonResponse, HttpRequest


# Create your views here.
def api_home(request: HttpRequest, *args, **kwargs):
    body = request.body.decode('utf-8')
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    print(data)
    # data['headers'] = request.META
    data['content_type'] = request.content_type
    return JsonResponse(data)

from django.shortcuts import render

from json import loads
from typing import Any
from django.http import HttpRequest, JsonResponse
from django.views import View
from django.utils.decorators import classonlymethod

from rest_framework.decorators import api_view


# class Views():
    
@api_view(["GET"])

def get_user_profile(request):
    # session_id = None
    # user_id = None
    # try:
    #     user_id = request.session['user_id']
    #     session_id = request.session['session_id']
    # except KeyError:
    #    pass
    # if user_id is None:
    response = {"status": "failure", "message": "user_id does not exist for this session id, invalid session id"}
    return JsonResponse(response)

        
from django.shortcuts import render

from json import loads
from typing import Any
from django.http import HttpRequest, JsonResponse
from django.views import View
from django.utils.decorators import classonlymethod
import json

from rest_framework.decorators import api_view
from chessProject.chess.chessRepo import chessRepo

# class Views():
    
@api_view(["POST"])

def get_chees_moves(request,slugName: str):
    payload = json.loads(request.body)
    response = chessRepo().set_working(payload,slugName)
    
    return JsonResponse(response)

        
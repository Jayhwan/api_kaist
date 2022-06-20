from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
import pandas as pd
from api import proc

def hello(request):
    return HttpResponse("<h1>Hello, world!</h1>")

class TestView(APIView):
    def get(self, request, format=None):
        name = request.query_params.get("name", "")
        if name is None:
            name = 'Jihwan Yu'
        age = request.query_params.get("age", "")
        return JsonResponse({'name': [name], 'age': [age]})

class PredictView(APIView):
    def get(self, request, format=None):
        gw = request.query_params.get("gw", "")
        dt = request.query_params.get("dt", "")
        url = request.query_params.get("url", "")
        starttime = request.query_params.get("starttime", "")
        endtime = request.query_params.get("endtime", "")

        if not gw or not url:
            gw = 1
            url = 'default'

        if not dt:
            starttime = proc.get_previous_24h()
            endtime =

        df = proc.call_predict(int(gw), dt)

        return JsonResponse(df)

class TestView(APIView):
    def get(self, request, format=None):
        name = request.query_params.get("name", "")
        if name is None:
            name = 'Jihwan Yu'
        age = request.query_params.get("age", "")
        return JsonResponse({'name': [name], 'age': [age]})

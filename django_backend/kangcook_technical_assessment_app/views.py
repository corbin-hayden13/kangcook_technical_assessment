from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views / apis here.


@api_view(["GET"])
def test_api_view(request):
    data = {"message": "Hello World!"}
    return Response(data)


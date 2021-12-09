from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

def hello_world_template(request):
    return render(request, 'accountapp/hello_world.html')


@api_view()
def hello_world(request):
    return Response({'message':'Hello world!!'})

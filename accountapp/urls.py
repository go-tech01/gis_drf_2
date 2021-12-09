from django.urls import path
from accountapp.views import hello_world, hello_world_template

app_name = 'accountapp'

urlpatterns = [
    path('hello_world_template/', hello_world_template, name='hello_world_template'),
    path('hello_world/', hello_world, name='hello_world'),
]

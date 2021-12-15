from django.urls import path
from profileapp.views import ProfileCreateAPIView, ProfileCreateTemplateView

app_name = 'profileapp'

urlpatterns = [
    path('', ProfileCreateAPIView.as_view(), name='create'),
    path('create_template/', ProfileCreateTemplateView.as_view(), name='create_template'),
]

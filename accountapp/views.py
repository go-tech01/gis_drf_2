from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from rest_framework import authentication, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

# UI 설정부분
from rest_framework.views import APIView

from accountapp.models import NewModel
from accountapp.permissions import IsOwner
from accountapp.serializes import NewModelSerializer, UserSerializer, UserWithoutPasswordSerializer


def hello_world_template(request):
    return render(request, 'accountapp/hello_world.html')

# 로직 처리부분
@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == "POST":
        input_data = request.data.get('input_data')
        new_model = NewModel()
        new_model.text = input_data
        new_model.save()
        # Serialize 하는 부분
        serializer = NewModelSerializer(new_model)
        return Response(serializer.data)
    new_model_list = NewModel.objects.all()
    serializer = NewModelSerializer(new_model_list, many=True)
    return Response(serializer.data)

def AccountCreateTemplate(request):
    return render(request, 'accountapp/create.html')

class AccountCreateAPIView(CreateAPIView):
    queryset = User.objects.all()          # model
    serializer_class = UserSerializer      # form class
    permission_classes = []                # 권한, 누구나 가입할 수 있도록 = [permissions.AllowAny]


# class ListUsers(APIView):
#     authentication_classes = [authentication.TokenAuthentication]
#     permission_classes = [permissions.IsAuthenticated]
#
#     def get(self, request, format=None):
#         usernames = [user.username for user in User.objects.all()]
#         return Response(usernames)


def AccountLoginView(request):
    return render(request, 'accountapp/login.html')

class AccountRetrieveTemplateView(TemplateView):
    template_name = 'accountapp/retrieve.html'

# class AccountRetrieveAPIView(RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserWithoutPasswordSerializer
#     permission_classes = [permissions.AllowAny]
#     authentication_classes = [TokenAuthentication]

class AccountUpdateTemplateView(TemplateView):
    template_name = 'accountapp/update.html'

# class AccountUpdateAPIView(UpdateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserWithoutPasswordSerializer   # form
#     permission_classes = [IsOwner]
#     authentication_classes = [TokenAuthentication]

class AccountDestroyTemplateView(TemplateView):
    template_name = 'accountapp/destroy.html'

# class AccountDestroyAPIView(DestroyAPIView):
#     queryset = User.objects.all()
#     permission_classes = [IsOwner]
#     authentication_classes = [TokenAuthentication]

class AccountRUDView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserWithoutPasswordSerializer
    permission_classes = [IsOwner]
    authentication_classes = [TokenAuthentication]
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        result_dict = dict(serializer.data)
        if request.user == instance:
            # serializer.data['is_page_owner'] = 'True'
            result_dict['is_page_owner'] = 'True'
        else:
            # serializer.data['is_page_owner'] = 'False'
            result_dict['is_page_owner'] = 'False'
        return Response(result_dict)


class AccountTokenRetrieveAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    http_method_names = ['get']                  # get만 사용할수 있음
    def get(self, request, *args, **kwargs):
        serializer = UserWithoutPasswordSerializer(request.user)
        return Response(serializer.data)
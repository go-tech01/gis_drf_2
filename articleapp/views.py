from django.shortcuts import render
from django.views.generic import TemplateView

from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, \
    ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from articleapp.models import Article
from articleapp.paginations import CustomPageNumberPagination
from articleapp.permissions import IsArticleOwner
from articleapp.serializers import ArticleSerializer

class ArticleCreateTemplateView(TemplateView):
    template_name = 'articleapp/create.html'

# class ArticleCreateAPIView(CreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [TokenAuthentication]
#     def perform_create(self, serializer):
#         serializer.save(writer=self.request.user)

class ArticleListTemplateView(TemplateView):
    template_name = 'articleapp/list.html'

# class ArticleListAPIView(ListAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     permission_classes = [AllowAny]
#     authentication_classes = [TokenAuthentication]
#     pagination_class = CustomPageNumberPagination

class ArticleListCreateAPIView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]
    pagination_class = CustomPageNumberPagination
    def perform_create(self, serializer):
        serializer.save(writer=self.request.user)
    def post(self, requset, *args, **kwargs):
        """
        Article 생성 Endpoint

        게시글 생성하기 위한 로직<br>
        게시글 생성하기 위해서는 로그인 권한을 요구합니다
        """
        return super().post(requset, *args, **kwargs)

class ArticleRetrieveTemplateView(TemplateView):
    template_name = 'articleapp/retrieve.html'

class ArticleUpdateTemplateView(TemplateView):
    template_name = 'articleapp/update.html'

class ArticleDestroyTemplateView(TemplateView):
    template_name = 'articleapp/destroy.html'

class ArticleRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsArticleOwner]
    authentication_classes = [TokenAuthentication]
    def get(self, request, *args, **kwargs):
        target_article = self.get_object()
        serializer = self.get_serializer(target_article)
        result_dict = dict(serializer.data)
        if target_article.writer == request.user:
            result_dict['is_page_owner'] = 'True'
        else:
            result_dict['is_page_owner'] = 'False'
        return Response(result_dict)
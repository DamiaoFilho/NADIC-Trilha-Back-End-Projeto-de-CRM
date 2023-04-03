from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework import permissions
from crm.models import *
from .serializers import *
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.contrib.auth import login, logout, authenticate
from django.core.exceptions import ValidationError

from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)

class stockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = stockSerializer

class userViewSet(ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


    permission_classes = [permissions.IsAuthenticated]

    @action(methods=['POST'], detail=False)
    def login(self, request):        
        username = request.data['username']
        password = request.data['password']
        print(password)

        authenticated_user = authenticate(self.request, username=username, password=password)

        if authenticated_user is not None:
            login(self.request, authenticated_user)
            authenticated_user = UserSerializer(authenticated_user)
            return Response('Success')
        else:
            raise ValidationError('Username or password incorrect')



    
class adminViewSet(ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
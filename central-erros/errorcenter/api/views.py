from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Log, Origin, Environment, Level
from .serializers import (LogSerializer, 
                          OriginSerializer, 
                          UserSerializer, 
                          EnvironmentSerializer,
                          LevelSerializer)
from .api_permissions import OnlyAdminCanList

from errorcenter.forms import SignUpForm

class LogApiViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Log.objects.all()
    serializer_class = LogSerializer

class OriginApiViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Origin.objects.all()
    serializer_class = OriginSerializer

class LevelApiViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
class EnvironmentListOnlyApiView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        queryset = Environment.objects.all()
        serializer = EnvironmentSerializer(queryset, many=True)
        return Response(serializer.data)

class UserApiViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, OnlyAdminCanList]

    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserToken(APIView):

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        
        if email is None or password is None:
            return Response({'error': 'Please provide both email and password'},
                            status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(username=email, password=password)
        
        if not user:
            return Response({'error': 'Invalid Credentials'}, 
                            status=status.HTTP_404_NOT_FOUND)
        
        token, _ = Token.objects.get_or_create(user=user)
       
        return Response({'token': token.key}, status=status.HTTP_200_OK)

def SignUp(request):
     if request.method == 'POST':
         form = SignUpForm(request.POST)
         if form.is_valid():
             form.save()
             return redirect('/api')
     else:
         form = SignUpForm()

         args = {'form': form}
         return render(request, 'api/signup.html', args)

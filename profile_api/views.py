from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profile_api import serializers
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from profile_api import models
from profile_api import permissions

from rest_framework.authentication import TokenAuthentication

class HelloApiView(APIView):
    """Test API VIEW"""

    serializer_class=serializers.HelloSerializer

    def get(self,request,format=None):
        """resturns a list of APIView features"""
        an_apiview=[
        'Uses HTTP methods as function (get,post,patch,put,delete)',
        'Is similar to a traditional Django View',
        'Gives you the most control over your application logic',
        'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello','an_apiview':an_apiview})

    def post(self,request,format=None):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handling updating an object"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """Handling a partial update of an object"""
        return Response({'method':'PATCH'})

    def delete(self,request, pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test APIViewswt"""
    serializer_class=serializers.HelloSerializer

    def list(self,request):
        """Return heelo message"""
        a_viewset = [
        'Uses actions(list,creat,retrive,upddate,partial update)',
        'Automativally maps to urls using router',
        'provides more functionality by less code'
        ]

        return Response({'message':'Hello','a_viewset':a_viewset})

    def create(self,request):
        """create a hello message"""
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response (
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def retrive(self,request,pk=None):
        """Handle getting an objecy by it's id"""
        return Response({'http_method':'GET'})

    def update(self,request, pk=None):
        """Handle updating an object"""
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        """Handle partiol updating"""
        return Response ({'http_method':'PUNCH'})

    def destroy(self,request,pk=None):
        """Handle the deleting of an object"""
        return Response({'http_method':'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """handling creating and updating file"""
    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)
    filter_backends=(filters.SearchFilter,)
    search_fields=('name','email',)


class UserLoginApiView(ObtainAuthToken):
    """Handling creating user authentication tokens"""
    renderer_classes= api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """handles creating reading and updating prfile feed items"""
    authentication_classes=(TokenAuthentication,)
    serializer_class=serializers.ProfileFeedItemSerializer
    queryset=models.UserFeedItem.objects.all()
    permission_classes=(
    permissions.UpdateOwnStatus,
    IsAuthenticated
    )

    def perform_create(self,serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)





# Create your views here.

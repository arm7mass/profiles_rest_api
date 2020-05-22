from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets




class HelloApiview(APIView):
    """ test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as functions (get, patch, put, delete',
            'Is similar to a traditional django view ',
            'Gives you the most control of your logic ',
            'is mapped manally to URLS',
        ]
        return Response({'message':'Helo','an_apiview':an_apiview})


    def post(self, request):
        """ create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """ Handle updatingan object"""
        return Response({'method': 'PUT'})
    
    def patch(self, request, pk=None):
        """ Handle partial update of object"""
        return Response({'method': 'PATCH'})
    
    def delete(self, request, pk=None):
        """ Delete an object"""
        return Response({'method': 'DELETE'})
    

class HelloViewSet(viewsets.ViewSet):
    """ Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, requst):
        """ Return Hello Message"""
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLS using Routrs',
            'Provides more functionality with less code '
        ]
        return Response({'message': 'Hello!', 'a_view':a_viewset})
    
    def create (self, request):
        """ create new hello message """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """ Handle getting an object by it is ID"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """ Handle updating the object"""
        return Response({'http_method':'PUT'})
    
    def partial_update(self, request, pk=None):
        """ Handle updating part of an object"""
        return Response({'http_method':'PATCH'})
    
    def destroy(self, request, pk=None):
        """ Handle removing an object"""
        return Response({'http_method':'DELETE'})

    

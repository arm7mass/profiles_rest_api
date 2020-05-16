from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers




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
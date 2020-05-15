from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiview(APIView):
    """ test API View"""
    def get(self, request, format=None):
        """ returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as functions (get, patch, put, delete',
            'Is similar to a traditional django view ',
            'Gives you the most control of your logic ',
            'is mapped manally to URLS',
        ]
        return Response({'message':'Helo','an_apiview':an_apiview})
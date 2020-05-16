from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """ Serialize a name field for testing out PIview"""
    name = serializers.CharField(max_length=10)
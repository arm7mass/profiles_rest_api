from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """ Serialize a name field for testing out PIview"""
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):

    # seriaize a user profile object
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password' : {
                'write_only' : True,
                'style':{'input_type':'password' }
            }
        }

    def create(self, validate_data):
        # create and return a new user 
        user = models.UserProfile.objects.create_user(
            email=validate_data['email'],
            name=validate_data['name'],
            password=validate_data['password']
        )
        return user

    
class ProfileFeedItemSerializer(serializers.ModelSerializer):
    # serilize profile feed item
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only':True}}

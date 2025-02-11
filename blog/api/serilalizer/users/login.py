from rest_framework import serializers
from django.contrib.auth import authenticate

class SrLogin(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    
    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        # Authenticate user
        user = authenticate(username=username, password=password)
        print(user)

        if user is None:
            raise serializers.ValidationError("Invalid username or Bad password.")

        if not user.is_active:
            raise serializers.ValidationError("User is not active.")

        return data
    

from rest_framework import serializers
from .models import Book
from django.contrib.auth.models import User
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields =('name', 'author')
 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)  
        return user

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from users.models import User

class UserModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username',
            'email'
        ]

class SignupSerializer(serializers.Serializer):

    email = serializers.EmailField(
        required=True,
        validators = [
            UniqueValidator(queryset=User.objects.all())
        ]
    )

    username = serializers.CharField(
        min_length=3,
        max_length=20,
        required=True,
        validators = [
            UniqueValidator(queryset=User.objects.all())
        ]
    )

    password = serializers.CharField(
        min_length=8,
        max_length=56,
        required=True
    )

    password_confirmation = serializers.CharField(
        min_length=8,
        max_length=56
    )

    def validate(self, data):
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError('password don\'t match')
        return data

    def create(self, data):
        user = User.objects.create_user(
            email=data['email'].lower(),
            username=data['username'],
            password=data['password']
        )
        return UserModelSerializer(user).data

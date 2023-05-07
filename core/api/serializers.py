from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'simple_name',
            'full_name',
        ]


class UserSerializer(UserNameSerializer):
    class Meta:
        model = User
        fields = UserNameSerializer.Meta.fields + [
            'username',
            'email',
            'role',
            'date_joined',
        ]


from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(required=True)
    username = serializers.CharField(required=True)

    class Meta:
        model = User
        exclude = ('password', 'is_admin', 'followed')

    def create(self, validated_data):
        name = validated_data.pop('username')
        password = validated_data.pop('password')
        return User.objects.create_user(username=name, password=password, **validated_data)


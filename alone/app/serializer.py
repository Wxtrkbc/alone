
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        exclude = ('is_admin', 'followed')

    def create(self, validated_data):
        name = validated_data.pop('name')
        password = validated_data.pop('password')
        return User.objects.create_user(username=name, password=password, **validated_data)


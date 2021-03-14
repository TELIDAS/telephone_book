from rest_framework import serializers
from user.models import Users


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ['id', 'username', 'first_name', 'last_name', 'user_type']
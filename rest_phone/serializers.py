from rest_framework import serializers
from phonebook.models import PhoneNumber


class PhoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = PhoneNumber
        fields = 'id number name'.split()

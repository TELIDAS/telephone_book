from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import Users


class RegisterApiView(APIView):

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = Users.objects.create(username=username,
                                    password=password,
                                    is_active=False)
        user.save()
        return Response(status=status.HTTP_201_CREATED)


class LoginApiView(APIView):
    def post(self, request):
        user = authenticate(username=request.data['username'],
                            password=request.data.get('password', 'admin123'))
        if not user:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={'message': 'User not found'})
        else:
            try:
                token = Token.objects.get(user=user)
            except Token.DoesNotExist:
                token = Token.objects.create(user=user)
            return Response(data={'token': token.key}, status=status.HTTP_201_CREATED)

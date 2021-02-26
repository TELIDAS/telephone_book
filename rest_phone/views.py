from django.db.models import Q
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from phonebook.models import PhoneNumber
from rest_phone.serializers import PhoneSerializer


class PhoneNumberAPIView(APIView, PageNumberPagination):
    allow_methods = ['GET', 'POST']
    serializer_class = PhoneSerializer

    def get(self, request, *args, **kwargs):
        query = request.query_params.get('query', '')
        phone = PhoneNumber.objects.filter(Q(number__contains=query) |
                                           Q(name__contains=query))
        results = self.paginate_queryset(phone,
                                         request,
                                         view=self)

        return self.get_paginated_response(
            self.serializer_class(results,
                                  many=True,
                                  context={'request': request}).data)

    def post(self, request):
        number = request.data.get('number')
        name = request.data.get('name')
        phone = PhoneNumber.objects.create(number=number,
                                           name=name)
        phone.save()
        return Response(data=self.serializer_class(phone).data,
                        status=status.HTTP_201_CREATED)


class PhoneNumberAPIViewDetail(APIView):
    allow_methods = ['GET', 'DELETE', 'PUT']
    serializer_class = PhoneSerializer

    def get(self, request, id):
        phone = PhoneNumber.objects.get(id=id)
        serializer = self.serializer_class(phone)
        return Response(data=serializer.data)

    def delete(self, request, *args, **kwargs):
        phone = PhoneNumber.objects.get(id=id)
        phone.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        phone = PhoneNumber.objects.get(id=id)
        number = request.data.get('number')
        name = request.data.get('name')
        phone.number = number
        phone.name = name
        phone.save()

        return Response(data=self.serializer_class(phone).data,
                        status=status.HTTP_200_OK)

from django.urls import path
from . import views as phone

urlpatterns = [
    path('api/v1/phone/', phone.PhoneNumberAPIView.as_view()),
    path('api/v1/phone/<int:id>/', phone.PhoneNumberAPIViewDetail.as_view()),
]
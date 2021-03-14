from django.urls import path
from . import views

urlpatterns = [
    path('', views.RegisterApiView.as_view()),
    path('api/v1/login/', views.LoginApiView.as_view()),

]
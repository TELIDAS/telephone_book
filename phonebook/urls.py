from django.urls import path

# from .parser import dj_bs
from .views import PhoneNumberDetailView, phones, SearchResultsView, SearchView

urlpatterns = [
    path('results/', SearchResultsView.as_view(), name='search_phones'),
    path('search/', SearchView.as_view(), name='home'),
    path('phone-numbers/', phones, name='phone'),
    path('phone-numbers/<int:pk>/', PhoneNumberDetailView.as_view()),

]
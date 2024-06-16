from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'countries'

urlpatterns = [
    path('', CountryListView.as_view(), name='country_list'),
    path('<int:pk>/', CountryDetailView.as_view(), name='country_detail'),
    path('<int:country_pk>/cities/', CityListView.as_view(), name='city_list'),
    path('<int:country_pk>/cities/<int:pk>/', CityDetailView.as_view(), name='city_detail'),
    path('cities/<int:pk>/landmarks/', LandmarkListView.as_view(), name='landmark_list'),
    path('landmarks/<int:pk>/', LandmarkDetailView.as_view(), name='landmark_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

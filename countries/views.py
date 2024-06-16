from django.views.generic import ListView, DetailView, TemplateView
from .models import Country, Landmark, City
from django.shortcuts import get_object_or_404, render

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['countries'] = Country.objects.all()
        return context
    
class CountryListView(ListView):
    model = Country
    template_name = 'countries/country_list.html'
    context_object_name = 'countries'

class CountryDetailView(DetailView):
    model = Country
    template_name = 'countries/country_detail.html'
    context_object_name = 'country'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        country = self.get_object()
        context['flag'] = country.flag
        return context

class LandmarkListView(ListView):
    model = Landmark
    template_name = 'countries/landmark_list.html'
    context_object_name = 'landmarks'

    def get_queryset(self):
        city = get_object_or_404(City, pk=self.kwargs['pk'])
        return Landmark.objects.filter(city=city)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city'] = get_object_or_404(City, pk=self.kwargs['pk'])
        return context

class LandmarkDetailView(DetailView):
    model = Landmark
    template_name = 'countries/landmark_detail.html'
    context_object_name = 'landmark'

class CityListView(ListView):
    template_name = 'countries/city_list.html'
    context_object_name = 'cities'

    def get_queryset(self):
        self.country = get_object_or_404(Country, pk=self.kwargs['country_pk'])
        return City.objects.filter(country=self.country)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['country'] = self.country
        return context

class CityDetailView(DetailView):
    model = City
    template_name = 'countries/city_detail.html'
    context_object_name = 'city'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        city = self.object
        context['landmarks'] = city.landmarks.all()
        return context
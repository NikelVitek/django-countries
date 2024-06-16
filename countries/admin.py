from django.contrib import admin
from .models import Country, City, Landmark
from django.utils.safestring import mark_safe
from django.utils.html import format_html

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'population')
    search_fields = ('name', 'country__name')
    list_filter = ('country',)

@admin.register(Landmark)
class LandmarkAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'description')
    search_fields = ('name', 'city__name')
    list_filter = ('city',)
    
@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'population', 'flag_display')
    def flag_display(self, obj):
        if obj.flag:
            return format_html(f'<img src="{obj.flag.url}" style="height: 50px;" />')
        else:
            return 'No flag'
        flag_display.short_description = 'Flag'
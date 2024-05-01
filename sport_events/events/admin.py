from django.contrib import admin
from .models import *
# Register your models here.



class EventsFilter(admin.ModelAdmin):

    list_display = ('city_city', 'address', 'description')
    search_fields = ['city', 'address']

    def city_city(self, obj):
        return obj.city.city

    city_city.short_description = 'Город проведения мероприятия'

admin.site.register(Events,EventsFilter )


class TypesFilter(admin.ModelAdmin):
    list_display = ('type', 'price')
    search_fields = ['type', 'price']

admin.site.register(Types_Events, TypesFilter)

class CitysFilter(admin.ModelAdmin):
    list_display = ('city',)
    search_fields = ['city',]

admin.site.register(Citys, CitysFilter)

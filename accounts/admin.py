from django.contrib import admin

# Register your models here.
from .models import Person, Country, City

admin.site.register(Country)
admin.site.register(City)
admin.site.register(Person)

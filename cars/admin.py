from django.contrib import admin

from cars.models import Car, CarModel, CarBrand

admin.site.register(CarBrand)
admin.site.register(CarModel)
admin.site.register(Car)

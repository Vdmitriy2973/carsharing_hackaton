from django.db import models
from django.utils.translation import gettext_lazy as _


class CarBrand(models.Model):
    """Производитель (брэнд) автомобилей"""
    name = models.CharField(max_length=100)
    description = models.TextField()
    foundation_date = models.DateField()


class CarModel(models.Model):
    """Модель автомобилей"""
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)


class Car(models.Model):
    """Автомобиль"""
    class CarType(models.TextChoices):
        ECONOMY = "EC", _('Economy')
        COMFORT = 'CF', _('Comfort')
        BUSINESS = 'BU', _('Business')

    number = models.CharField(max_length=10, unique=True, verbose_name=_('Number'))
    type = models.CharField(max_length=2, choices=CarType.choices, default=CarType.ECONOMY)
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    production_year = models.IntegerField()

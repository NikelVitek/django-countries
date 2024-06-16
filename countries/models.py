from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100, verbose_name='Country Name')
    population = models.IntegerField(verbose_name='Population')
    area = models.FloatField(verbose_name='Area')

    def custom_upload(instance, filename):
        return f'flags/{instance.name}.png'

    flag = models.ImageField(upload_to=custom_upload, default='default_flag.png', verbose_name='Flag')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

class City(models.Model):
    name = models.CharField(max_length=100, verbose_name='City Name')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cities', verbose_name='Country')
    population = models.IntegerField(verbose_name='Population')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

class Landmark(models.Model):
    name = models.CharField(max_length=100, verbose_name='Landmark Name')
    description = models.TextField(verbose_name='Description')
    city = models.ForeignKey(City, related_name='landmarks', on_delete=models.CASCADE, verbose_name='City')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Landmark'
        verbose_name_plural = 'Landmarks'

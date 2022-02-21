from django.db import models


class Car(models.Model):
    uuid = models.CharField('Uniq ID', unique=True, max_length=20)
    car_category = models.CharField('Car category', max_length=2)
    brand_id = models.CharField('Brand ID', max_length=20)
    year_from = models.DateField('Year from')
    year_to = models.DateField('Year to')
    brand = models.CharField('Brand of car', max_length=25)
    mark_id = models.CharField('Mark ID', max_length=25)
    mark = models.CharField('Mark', max_length=25)
    cyrillic_mark = models.CharField('Mark name in russia', max_length=25)
    model = models.CharField('Model of car', max_length=25)
    cyrillic_model = models.CharField('Model name in russia', max_length=25)
    eng_power = models.IntegerField('Engine Power')
    horse_power = models.IntegerField('Horse Power')

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

    def __str__(self):
        return self.brand


from django.db import models
import datetime

class Citys(models.Model):
    city = models.CharField(max_length=100, verbose_name='Город, в котором предоставляется услуга проведения спортивного мероприятия', null=False, blank=False)

    class Meta:
        verbose_name = "Города предоставления услуг"
        verbose_name_plural = "Города предоставления услуг"

    def __str__(self):
        return self.city

class Types_Events(models.Model):
    type = models.CharField(max_length=100, verbose_name='Тип спортивного мероприятия', null=False, blank=False)
    price = models.FloatField(verbose_name='Минимальная стоимость', null=False, blank=False)

    class Meta:
        verbose_name = "Типы спортивных мероприятий"
        verbose_name_plural = "Типы спортивных мероприятий"
    def __str__(self):
        return self.type

class Events(models.Model):
    city = models.ForeignKey(Citys, models.SET_NULL, blank=True, null=True, verbose_name='Город проведения спортивного мероприятия')
    address = models.CharField(max_length=255, verbose_name='Адрес проведения спортивного мероприятия')
    description = models.CharField(max_length=255, verbose_name='Описание спортивного мероприятия')

    date_order = models.DateTimeField(verbose_name='Дата и время оформления заказа на проведение спортивного мероприятия', default=datetime.datetime.now(), blank=True, null=False)
    date_start = models.DateTimeField(verbose_name='Дата и время проведения спортивного мероприятия', blank=False, null=False)
    date_end = models.DateTimeField(verbose_name='Дата и время окончания спортивного мероприятия', blank=False, null=False)

    type = models.ForeignKey(Types_Events, models.SET_NULL, blank=True, null=True, verbose_name='Тип спортивного мероприятия')
    budget = models.FloatField(verbose_name='Бюджет организатора', null=False, blank=False)

    list_display = ('city', 'address', 'description')
    search_fields = ['address', 'city']

    class Meta:
        verbose_name = "Спортивные мероприятия"
        verbose_name_plural = "Спортивные мероприятия"

    def __str__(self):
        return 'Город: ' + self.city.city + ', адрес: ' + self.address








import datetime
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone

# Create your models here.
from django.utils.timezone import now


class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField('Наименование продукта', max_length=200)
    product_unit = models.CharField('Ед. измерения', max_length=200)
    product_price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    product_description = models.TextField('Описание продукта')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'id: {self.product_id}, product_name: {self.product_name}'


class Areas(models.Model):
    area_id = models.AutoField(primary_key=True)
    area_name = models.CharField('Наименование района', max_length=200)
    area_price = models.DecimalField('Стоимость доставки', default=0, max_digits=10, decimal_places=2, null=True, blank=True)
    area_description = models.TextField('Описание района')

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'

    def __str__(self):
        return f'id: {self.area_id}, area_name: {self.area_name}'


class OrderStatus(models.Model):
    status_id = models.AutoField(primary_key=True)
    status_name = models.CharField('Наименование статуса', max_length=200)

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказов'

    def __str__(self):
        return f'id: {self.status_id}, status_name: {self.status_name}'


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, db_column="id", on_delete=models.CASCADE)
    # user_id = models.ForeignKey(User, db_column="user", on_delete=models.CASCADE)
    # user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order_date = models.DateTimeField('Дата заказа', default=timezone.now())
    order_timezone = models.CharField('Timezone', max_length=6)
    order_name = models.CharField('Имя заказчика', max_length=200)
    order_phone = models.CharField('Телефон заказчика', max_length=200)
    product_id = models.ForeignKey(Products, db_column="product_id", on_delete=models.CASCADE)
    order_count = models.DecimalField('Количество', max_digits=10, decimal_places=2)
    area_id = models.ForeignKey(Areas, db_column="area_id", on_delete=models.CASCADE)
    order_address = models.CharField('Адрес доставки', max_length=500)
    order_date_delivery = models.DateField('Дата доставки')
    order_time_delivery = models.TimeField('Время доставки')
    order_description = models.TextField('Описание заказа', null=True, blank=True)
    order_cost = models.DecimalField('Стоимость', max_digits=10, decimal_places=2)
    # не даст удалить статус, пока есть заказы по нему
    status_id = models.ForeignKey(OrderStatus, db_column="status_id", default=1, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'id: {self.order_id}, order_phone: {self.order_phone}, order_name: {self.order_name}'

    def is_overdue_order(self):
        '''
        Проверка на просроченный заказ
        Если через 1 час после создания, заявка все еще в статуса Новый или Не определено
        '''
        return self.status_id in (1, 2) and (self.order_date  >= (timezone.now() - datetime.timedelta(hours=1)))

    def get_status_name(self):
        ''' Получаем наименование статуса по id '''
        pass

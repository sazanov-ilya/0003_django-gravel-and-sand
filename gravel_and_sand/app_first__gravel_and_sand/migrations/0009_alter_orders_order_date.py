# Generated by Django 3.2.5 on 2021-07-28 14:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app_first__gravel_and_sand', '0008_auto_20210727_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 28, 14, 23, 14, 68238, tzinfo=utc), verbose_name='Дата заказа'),
        ),
    ]
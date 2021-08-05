# Generated by Django 3.2.5 on 2021-07-28 14:38

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_first__gravel_and_sand', '0011_auto_20210728_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 28, 14, 38, 51, 574963, tzinfo=utc), verbose_name='Дата заказа'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='user_id',
            field=models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 3.2.5 on 2021-07-28 19:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_first__gravel_and_sand', '0016_alter_orders_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='user_id',
            field=models.ForeignKey(db_column='id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

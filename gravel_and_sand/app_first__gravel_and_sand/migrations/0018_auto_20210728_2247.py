# Generated by Django 3.2.5 on 2021-07-28 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_first__gravel_and_sand', '0017_alter_orders_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='area_id',
            field=models.ForeignKey(db_column='area_id', on_delete=django.db.models.deletion.CASCADE, to='app_first__gravel_and_sand.areas'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='product_id',
            field=models.ForeignKey(db_column='product_id', on_delete=django.db.models.deletion.CASCADE, to='app_first__gravel_and_sand.products'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='status_id',
            field=models.ForeignKey(db_column='status_id', default=1, on_delete=django.db.models.deletion.PROTECT, to='app_first__gravel_and_sand.orderstatus'),
        ),
    ]
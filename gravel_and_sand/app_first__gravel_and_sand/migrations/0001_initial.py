# Generated by Django 3.2.5 on 2021-07-14 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=200, verbose_name='Наименование продукта')),
                ('product_unit', models.CharField(max_length=200, verbose_name='Ед. измерения')),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Стоимость')),
                ('product_description', models.TextField(verbose_name='Описание')),
            ],
        ),
    ]

# Generated by Django 3.0.7 on 2020-06-22 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='gtin',
            field=models.BigIntegerField(default=0),
        ),
    ]

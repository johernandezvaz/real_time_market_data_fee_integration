# Generated by Django 4.2.7 on 2024-01-22 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market_data', '0004_alter_marketdata_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketdata',
            name='timestamp',
            field=models.IntegerField(),
        ),
    ]

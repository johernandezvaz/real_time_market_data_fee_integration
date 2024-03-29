# Generated by Django 4.2.7 on 2024-01-22 17:59

from django.db import migrations
from datetime import datetime

def convert_unix_timestamps_to_date_format(apps, schema_editor):
    MarketData = apps.get_model('market_data', 'MarketData')

    for data in MarketData.objects.all():
        # Assuming timestamp is a UNIX timestamp (seconds since epoch)
        unix_timestamp = data.timestamp.timestamp()

        # Convert to 'YYYY-MM-DD' format
        formatted_date = datetime.utcfromtimestamp(unix_timestamp).strftime('%Y-%m-%d')

        # Update the timestamp in the model
        data.timestamp = formatted_date
        data.save()


class Migration(migrations.Migration):

    dependencies = [
        ('market_data', '0002_delete_exchange_marketdata_exchange'),
    ]

    operations = [
         migrations.RunPython(convert_unix_timestamps_to_date_format),
    ]

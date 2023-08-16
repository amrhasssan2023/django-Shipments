# Generated by Django 4.2.4 on 2023-08-07 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0002_shipemttrak'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShipmentStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipment_status', models.CharField(choices=[('Available', 'Available'), ('Unavailable', 'Unavailable')], max_length=250)),
                ('decription', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]

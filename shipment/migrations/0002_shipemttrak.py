# Generated by Django 4.2.4 on 2023-08-07 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShipemtTrak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trak', models.CharField(max_length=120)),
                ('courier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipment', to='shipment.courier')),
            ],
        ),
    ]

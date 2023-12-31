# Generated by Django 4.2.4 on 2023-08-07 10:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import django_measurement.models
import measurement.measures.distance
import measurement.measures.mass
import measurement.measures.volume
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shipment', '0003_shipmentstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipmentstatus',
            name='shipment_status',
            field=models.CharField(choices=[('Deliverd', 'Deliverd'), ('Canceled', 'Canceled')], max_length=250),
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipment_name', models.CharField(max_length=150)),
                ('sender_address', models.TextField(blank=True, max_length=500, null=True)),
                ('sender_country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('sender_phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('receiver_address', models.TextField(max_length=500)),
                ('receiver_country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('receiver_phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('shipment_Content', models.TextField(max_length=150)),
                ('number_of_pieces', models.IntegerField()),
                ('volume', django_measurement.models.MeasurementField(measurement=measurement.measures.volume.Volume)),
                ('sides', django_measurement.models.MeasurementField(measurement=measurement.measures.distance.Distance)),
                ('material_size', django_measurement.models.MeasurementField(measurement=measurement.measures.distance.Area)),
                ('max_weight', django_measurement.models.MeasurementField(measurement=measurement.measures.mass.Mass)),
                ('courier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courier', to='shipment.courier')),
                ('shimpemt_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shipment.shipmentstatus')),
                ('shimpemt_trak', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shipment.shipemttrak')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

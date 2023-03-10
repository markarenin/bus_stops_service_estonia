# Generated by Django 4.1.4 on 2022-12-16 15:36

import api.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.CharField(default=api.models.generate_random_string, max_length=32, primary_key=True, serialize=False)),
                ('agency_id', models.IntegerField()),
                ('route_short_name', models.CharField(max_length=32)),
                ('route_long_name', models.CharField(max_length=1024)),
                ('route_type', models.IntegerField()),
                ('route_color', models.CharField(max_length=8)),
                ('route_desc', models.CharField(max_length=1024)),
                ('competent_authority', models.CharField(max_length=64, null=True)),
            ],
            options={
                'db_table': 'routes',
            },
        ),
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stop_code', models.CharField(blank=True, max_length=255, null=True)),
                ('stop_lat', models.FloatField()),
                ('stop_lon', models.FloatField()),
                ('zone_id', models.IntegerField()),
                ('alias', models.CharField(blank=True, max_length=255, null=True)),
                ('stop_area', models.CharField(blank=True, max_length=255, null=True)),
                ('stop_desc', models.CharField(blank=True, max_length=255, null=True)),
                ('lest_x', models.IntegerField()),
                ('lest_y', models.IntegerField()),
                ('zone_name', models.CharField(blank=True, max_length=255, null=True)),
                ('authority', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'stops',
            },
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_id', models.IntegerField()),
                ('trip_headsign', models.CharField(max_length=64)),
                ('trip_long_name', models.CharField(max_length=1024)),
                ('direction_code', models.IntegerField()),
                ('route_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.route')),
            ],
            options={
                'db_table': 'trips',
            },
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrival_time', models.TimeField()),
                ('departure_time', models.TimeField()),
                ('stop_sequence', models.IntegerField()),
                ('pickup_type', models.IntegerField()),
                ('drop_off_type', models.IntegerField()),
                ('stop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='times', to='api.stop')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='times', to='api.trip')),
            ],
            options={
                'db_table': 'times',
            },
        ),
    ]

# Generated by Django 4.1.4 on 2022-12-17 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_stop_lest_x_alter_stop_lest_y'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stoptime',
            name='trip',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='times', to='api.trip'),
        ),
    ]

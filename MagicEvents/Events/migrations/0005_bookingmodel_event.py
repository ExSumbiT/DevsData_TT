# Generated by Django 4.1.5 on 2023-01-31 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0004_rename_u_date_bookingmodel_c_date_eventmodel_c_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingmodel',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Events.eventmodel'),
        ),
    ]

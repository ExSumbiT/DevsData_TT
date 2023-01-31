# Generated by Django 4.1.5 on 2023-01-31 16:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0003_bookingmodel_u_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookingmodel',
            old_name='u_date',
            new_name='c_date',
        ),
        migrations.AddField(
            model_name='eventmodel',
            name='c_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bookingmodel',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('canceled', 'Canceled')], default='active', max_length=10),
        ),
    ]

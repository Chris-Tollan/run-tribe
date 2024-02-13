# Generated by Django 4.2.9 on 2024-02-13 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runs', '0002_booking'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={},
        ),
        migrations.RemoveField(
            model_name='booking',
            name='available_date',
        ),
        migrations.AddField(
            model_name='booking',
            name='phone',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]

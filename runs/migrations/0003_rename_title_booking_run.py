# Generated by Django 4.2.9 on 2024-02-24 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('runs', '0002_runs_featured_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='title',
            new_name='run',
        ),
    ]

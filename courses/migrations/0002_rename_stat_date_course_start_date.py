# Generated by Django 4.2.6 on 2023-11-03 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='stat_date',
            new_name='start_date',
        ),
    ]
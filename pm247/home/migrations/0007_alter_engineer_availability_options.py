# Generated by Django 5.0 on 2024-05-13 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_engineer_availability_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='engineer_availability',
            options={'permissions': [('view_engineers_today', 'Can view engineers available today'), ('view_index', 'Can view index')]},
        ),
    ]
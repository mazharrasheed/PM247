# Generated by Django 5.0 on 2024-05-13 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_delete_userwithengineeravailability_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='engineer_availability',
            options={'permissions': [('view_engineers_today', 'Can view engineers available today')]},
        ),
    ]
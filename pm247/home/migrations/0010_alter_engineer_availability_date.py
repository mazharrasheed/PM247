# Generated by Django 5.0 on 2024-05-14 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_engineer_availability_date_alter_job_type_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engineer_availability',
            name='date',
            field=models.DateField(null=True),
        ),
    ]

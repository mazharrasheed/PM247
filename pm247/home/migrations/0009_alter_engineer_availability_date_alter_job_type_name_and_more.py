# Generated by Django 5.0 on 2024-05-14 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_engineer_availability_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engineer_availability',
            name='date',
            field=models.DateField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='job_type',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='post_code',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]

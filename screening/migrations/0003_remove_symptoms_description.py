# Generated by Django 3.2.6 on 2021-08-08 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('screening', '0002_patient_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='symptoms',
            name='description',
        ),
    ]

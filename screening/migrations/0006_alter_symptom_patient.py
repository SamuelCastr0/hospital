# Generated by Django 3.2.6 on 2021-08-11 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('screening', '0005_auto_20210809_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='symptom',
            name='patient',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='screening.patient'),
        ),
    ]
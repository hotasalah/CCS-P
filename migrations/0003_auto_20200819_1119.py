# Generated by Django 3.0.5 on 2020-08-19 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concrete', '0002_auto_20200819_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predictmodel',
            name='compressive_strength',
            field=models.FloatField(default=0.0),
        ),
    ]

# Generated by Django 3.0.8 on 2020-07-24 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_auto_20200724_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowbook',
            name='status',
            field=models.CharField(max_length=50),
        ),
    ]

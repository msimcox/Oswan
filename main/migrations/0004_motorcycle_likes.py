# Generated by Django 3.1.6 on 2021-04-25 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210422_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='motorcycle',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]

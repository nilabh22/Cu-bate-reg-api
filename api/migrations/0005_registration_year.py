# Generated by Django 3.2.6 on 2022-07-16 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20220713_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='year',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

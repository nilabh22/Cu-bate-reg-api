# Generated by Django 3.2.6 on 2022-07-16 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_registration_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
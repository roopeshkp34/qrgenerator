# Generated by Django 3.2.5 on 2021-07-18 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]

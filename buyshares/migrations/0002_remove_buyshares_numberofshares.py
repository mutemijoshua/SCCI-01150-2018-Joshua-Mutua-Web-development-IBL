# Generated by Django 5.0.6 on 2024-09-09 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buyshares', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyshares',
            name='numberofshares',
        ),
    ]

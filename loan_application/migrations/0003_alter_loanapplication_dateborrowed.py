# Generated by Django 5.0.6 on 2024-09-08 12:22

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan_application', '0002_rename_amount_loanapplication_amountb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanapplication',
            name='Dateborrowed',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

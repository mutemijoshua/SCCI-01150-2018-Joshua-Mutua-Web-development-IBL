# Generated by Django 5.0.6 on 2024-08-22 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loan_application', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loanapplication',
            old_name='amount',
            new_name='amountb',
        ),
    ]

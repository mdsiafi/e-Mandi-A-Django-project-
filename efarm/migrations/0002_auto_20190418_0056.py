# Generated by Django 2.1 on 2019-04-17 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('efarm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='type',
            field=models.CharField(choices=[('customer', 'Customer'), ('farmer', 'Farmer')], max_length=254),
        ),
    ]

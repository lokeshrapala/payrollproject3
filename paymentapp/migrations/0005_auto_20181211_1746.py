# Generated by Django 2.0.7 on 2018-12-11 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paymentapp', '0004_auto_20181211_1744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emp_data',
            name='id',
        ),
        migrations.RemoveField(
            model_name='finance_data',
            name='id',
        ),
        migrations.AlterField(
            model_name='emp_data',
            name='empid',
            field=models.CharField(max_length=7, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='finance_data',
            name='acid',
            field=models.CharField(max_length=7, primary_key=True, serialize=False),
        ),
    ]

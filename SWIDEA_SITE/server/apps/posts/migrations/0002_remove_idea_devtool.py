# Generated by Django 4.1.5 on 2023-01-18 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='idea',
            name='devtool',
        ),
    ]
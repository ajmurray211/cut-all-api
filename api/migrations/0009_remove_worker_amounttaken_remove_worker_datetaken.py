# Generated by Django 4.1 on 2022-08-24 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_part_workerkey'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worker',
            name='amountTaken',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='dateTaken',
        ),
    ]
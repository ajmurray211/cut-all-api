# Generated by Django 4.1 on 2022-08-22 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='onHand',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
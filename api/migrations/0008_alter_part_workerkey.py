# Generated by Django 4.1 on 2022-08-24 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_part_workerkey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='workerKey',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='workeKey', to='api.worker'),
        ),
    ]

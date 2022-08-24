# Generated by Django 4.1 on 2022-08-23 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_part_workerkey_part_workerkey'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='part',
            name='workerKey',
        ),
        migrations.AddField(
            model_name='part',
            name='workerKey',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='workeKey', to='api.worker'),
        ),
    ]
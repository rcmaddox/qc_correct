# Generated by Django 3.2.8 on 2021-10-22 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0008_rename_mix_size_choices_jmf_mix_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='corereadings',
            name='date_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='qcreport',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]

# Generated by Django 3.2.8 on 2021-11-02 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0023_auto_20211102_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corereadings',
            name='gauge_reading_1',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='corereadings',
            name='gauge_reading_2',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='corereadings',
            name='gauge_reading_3',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='corereadings',
            name='gauge_reading_4',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='corereadings',
            name='gauge_reading_5',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]

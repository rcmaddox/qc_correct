# Generated by Django 3.2.8 on 2021-10-21 04:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoreReadings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_type', models.CharField(max_length=10)),
                ('core_location', models.CharField(max_length=30)),
                ('lane_direction', models.CharField(max_length=30)),
                ('gauge_reading_1', models.CharField(max_length=10)),
                ('gauge_reading_2', models.CharField(max_length=10)),
                ('gauge_reading_3', models.CharField(max_length=10)),
                ('gauge_reading_4', models.CharField(max_length=10)),
                ('gauge_reading_5', models.CharField(max_length=10)),
                ('gauge_reading_average', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='JMF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jmf_number', models.CharField(max_length=20)),
                ('gmm', models.CharField(max_length=10)),
                ('gauge_density', models.CharField(max_length=10)),
                ('pdf', models.FileField(upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barber_number', models.CharField(max_length=10)),
                ('state_number', models.CharField(max_length=15)),
                ('project_name', models.CharField(max_length=50)),
                ('jmfs', models.ManyToManyField(to='reports.JMF')),
            ],
        ),
        migrations.CreateModel(
            name='QCReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField(blank=True, null=True)),
                ('jmf', models.ManyToManyField(to='reports.JMF')),
                ('project', models.ManyToManyField(to='reports.Project')),
                ('readings', models.ManyToManyField(to='reports.CoreReadings')),
            ],
        ),
        migrations.AddField(
            model_name='corereadings',
            name='jmf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.jmf'),
        ),
        migrations.AddField(
            model_name='corereadings',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.project'),
        ),
    ]

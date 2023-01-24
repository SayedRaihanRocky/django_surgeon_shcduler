# Generated by Django 4.1.3 on 2022-11-04 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='anesthesiologist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_code', models.CharField(max_length=20)),
                ('a_name', models.CharField(max_length=100)),
                ('a_email', models.EmailField(max_length=254)),
                ('a_contact', models.CharField(max_length=15)),
                ('a_address', models.CharField(max_length=250)),
                ('a_highest_degree', models.CharField(max_length=150)),
                ('rate_per_day', models.FloatField()),
                ('rate_per_surgery', models.FloatField()),
                ('sg_status', models.BooleanField()),
            ],
            options={
                'db_table': 'infoanesthesiologist',
            },
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-04 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_code', models.CharField(max_length=20)),
                ('p_fname', models.CharField(max_length=100)),
                ('p_lname', models.CharField(max_length=100)),
                ('p_contact', models.CharField(max_length=200)),
                ('p_email', models.EmailField(max_length=254)),
                ('p_dob', models.DateField()),
                ('p_address', models.CharField(max_length=250)),
                ('p_insuarance_id', models.CharField(max_length=150)),
                ('p_insuarance_name', models.CharField(max_length=150)),
                ('p_status', models.BooleanField()),
            ],
            options={
                'db_table': 'infopateint',
            },
        ),
    ]

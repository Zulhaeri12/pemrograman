# Generated by Django 4.2 on 2023-05-05 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='jadwalModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tanggal', models.CharField(max_length=50)),
                ('Imsyak', models.TimeField()),
                ('Subuh', models.TimeField()),
                ('Terbit', models.TimeField()),
                ('Dhuha', models.TimeField()),
                ('Dzuhur', models.TimeField()),
                ('Asar', models.TimeField()),
                ('Magrib', models.TimeField()),
                ('Isya', models.TimeField()),
            ],
        ),
    ]

# Generated by Django 4.1.4 on 2022-12-14 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
                ('seats', models.IntegerField()),
                ('body', models.CharField(max_length=20)),
                ('engine_volume', models.FloatField()),
            ],
            options={
                'db_table': 'cars',
            },
        ),
    ]
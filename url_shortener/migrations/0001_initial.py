# Generated by Django 3.0.2 on 2020-02-02 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrlMappingTable',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False, unique=True)),
                ('url', models.TextField()),
            ],
        ),
    ]

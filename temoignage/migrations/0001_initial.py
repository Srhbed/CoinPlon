# Generated by Django 4.1.2 on 2022-10-12 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Temoignage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.TimeField(max_length=500)),
                ('author', models.CharField(max_length=500)),
            ],
        ),
    ]
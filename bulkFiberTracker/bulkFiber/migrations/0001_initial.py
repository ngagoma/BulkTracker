# Generated by Django 3.2.9 on 2021-12-03 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataHall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='DH Name')),
                ('dh_site_code', models.CharField(max_length=15, verbose_name='DH Code')),
            ],
        ),
    ]
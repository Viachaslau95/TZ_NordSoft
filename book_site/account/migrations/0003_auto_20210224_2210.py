# Generated by Django 3.1.6 on 2021-02-24 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20210224_2122'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'ordering': ['first_name'], 'verbose_name': 'Аккаунт', 'verbose_name_plural': 'Аккаунты'},
        ),
    ]
# Generated by Django 3.1.6 on 2021-02-09 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-id'], 'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название '),
        ),
        migrations.AlterField(
            model_name='book',
            name='number',
            field=models.PositiveIntegerField(verbose_name='остаток'),
        ),
        migrations.AlterField(
            model_name='book',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y,%m/%d/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена'),
        ),
    ]

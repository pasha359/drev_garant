# Generated by Django 4.1.7 on 2023-03-11 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_wood_is_published_alter_wood_currency_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published', models.BooleanField(default=False, verbose_name='Опубликован')),
                ('name', models.CharField(max_length=50, verbose_name='Ключевое слово')),
            ],
            options={
                'verbose_name': 'Ключевое слово',
                'verbose_name_plural': 'Ключевые слова',
            },
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='wood',
            name='unit',
            field=models.CharField(choices=[('m3', '1м.куб.')], default='1m3', max_length=10, verbose_name='Количество'),
        ),
    ]

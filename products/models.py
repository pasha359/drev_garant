from django.db import models

class PublishedMixin(models.Model):
    published = models.BooleanField(verbose_name='Опубликован', default=True)

    class Meta:
        abstract = True


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    image = models.ImageField(upload_to='images', blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Wood(PublishedMixin):

    currency = (
        ('BYN', 'byn'),
    )

    unit = (
        ('m3', '1м.куб.'),
    )

    grade = (
        (int('0'),'0'),
        (int('1'), '1'),
        (int('2'), '2'),
        (int('3'), '3'),
        (int('4'), '4'),

    )

    name = models.CharField(max_length=100, verbose_name='Название пиломатериалов')
    thickness = models.CharField(max_length=10, blank=True, help_text='мм', verbose_name='Толщина')
    grade = models.IntegerField(verbose_name='Сорт', choices=grade)
    price = models.CharField(max_length=100, verbose_name='Цена')
    currency = models.CharField(max_length=20,verbose_name='Валюта', choices=currency, null=True, blank=True)
    unit = models.CharField(max_length=10, choices=unit,default='1m3',verbose_name='Количество')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Keyword(PublishedMixin):
    name = models.CharField(max_length=50, verbose_name='Ключевое слово')

    class Meta:
        verbose_name = 'Ключевое слово'
        verbose_name_plural = 'Ключевые слова'

    def __str__(self):
        return self.name

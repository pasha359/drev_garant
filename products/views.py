from django.shortcuts import render
from .models import Wood

def home (request):
    wood_ash = Wood.objects.filter(category__name='Доска Ясеня')
    wood_oak = Wood.objects.filter(category__name='Доска Дуба')
    wood_birch = Wood.objects.filter(category__name='Доска Лиственных Пород (Береза)')
    wood_alder = Wood.objects.filter(category__name='Доска Лиственных Пород (Ольха)')
    wood_needles = Wood.objects.filter(category__name='П/М НЕОБРЕЗНЫЕ ХВОЙНЫХ ПОРОД')

    context = {
        'wood_ash': wood_ash,
        'wood_oak': wood_oak,
        'wood_birch': wood_birch,
        'wood_alder': wood_alder,
        'wood_needles': wood_needles

    }
    return render(request, 'products/index.html', context)

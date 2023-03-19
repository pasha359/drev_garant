from django.shortcuts import render
from .models import Category, Wood, Photo
from django.db.models import Prefetch

def home (request):
    queryset = Wood.objects.filter(published=True)
    query = Category.objects.prefetch_related(
        Prefetch('woods', queryset=queryset))

    context = {
        'query': query,
}
    return render(request, 'products/index.html', context)

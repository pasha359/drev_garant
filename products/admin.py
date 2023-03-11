from django.contrib import admin
from .models import Category, Wood, Keyword

class WoodAdmin(admin.StackedInline):
    model = Wood

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ['name', 'image']
    inlines = [WoodAdmin, ]

class KeywordAdmin(admin.ModelAdmin):
    model = Keyword
    list_display = ['name', 'published']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Keyword, KeywordAdmin)






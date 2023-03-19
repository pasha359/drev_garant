from django.contrib import admin
from .models import Category, Wood, Keyword, Photo

class WoodAdmin(admin.StackedInline):
    model = Wood

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ['name', 'image']
    inlines = [WoodAdmin, ]

class KeywordAdmin(admin.ModelAdmin):
    model = Keyword
    list_display = ['name', 'published']

class PhotoAdmin(admin.ModelAdmin):
    model = Photo
    list_display = ['name', 'image']



admin.site.register(Category, CategoryAdmin)
admin.site.register(Keyword, KeywordAdmin)
admin.site.register(Photo, PhotoAdmin)






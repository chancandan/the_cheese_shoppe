from django.contrib import admin
from .models import Product, Category
from .models import Favorite


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'added_at')
    ordering = ('-added_at',)

admin.site.register(Favorite, FavoriteAdmin)
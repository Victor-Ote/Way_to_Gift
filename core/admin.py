from django.contrib import admin

from .models import Category, Gift

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'modified_at')

@admin.register(Gift)
class GiftAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'created_at', 'modified_at')
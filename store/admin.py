from django.contrib import admin
from .models import Category,Product

# Category Admin
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ['category_name','slug']
    ordering = ['category_name']
admin.site.register(Category,CategoryAdmin)

# Product Admin
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = ('product_name','category','is_available',)
    ordering = ['-created_date']

admin.site.register(Product,ProductAdmin)

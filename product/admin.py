from django.contrib import admin

from product.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('ean','description','price','category')
    list_filter = ('category',)
    search_fields = ('ean','description')

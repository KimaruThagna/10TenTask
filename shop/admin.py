from django.contrib import admin
from .models import *
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('lastUpdated', 'addedOn','addedBy')
    list_display = ('addedBy','name','quantity','pricePerKg')
    list_editable =('name','quantity','pricePerKg')
    search_fields = ('name',)
    list_filter = ('quantity',)

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)
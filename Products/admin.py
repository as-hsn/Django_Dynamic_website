from django.contrib import admin
from Products.models import  AllProduct
from Products.models import  TopProduct

# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    list_display=('product_title', 'product_image', 'product_description', 'old_price','new_price', 'product_tag')
    


admin.site.register(AllProduct, ServiceAdmin)   
admin.site.register(TopProduct, ServiceAdmin)  

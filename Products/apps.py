from django.apps import AppConfig


class AllProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'all_products'
    
class TopProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'top_product'

from django.contrib import admin
from blog.models import  Blog

# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    list_display=('blog_title', 'blog_description', 'blog_image', 'blog_tag')
    
admin.site.register(Blog, ServiceAdmin)   
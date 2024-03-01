from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from autoslug import AutoSlugField

# Create your models here.

class Blog(models.Model):
    blog_title= models.CharField(max_length=100, unique=True)
    blog_description= CKEditor5Field('Text', config_name='extends')
    blog_image= models.ImageField(upload_to='media', max_length=350, null=False, default=None)
    blog_tag= models.CharField(max_length=50, null=True, blank=True, default='Blog')
    blog_slug= AutoSlugField(populate_from='blog_title', unique=True, null=True,)
    
    
    def save(self, *args, **kwargs):
        # Check if an image is already associated with this instance
        if self.pk:
            try:
                old_instance = Blog.objects.get(pk=self.pk)
                # Check if the image has changed
                if self.blog_image and old_instance.blog_image != self.blog_image:
                    old_instance.blog_image.delete()
            except Blog.DoesNotExist:
                pass  # Handle the case where the instance doesn't exist yet

        self.blog_slug = None  # Set to None to trigger a new slug creation
        super(Blog, self).save(*args, **kwargs)
        
    
    
    def delete(self, *args, **kwargs):
        self.blog_image.delete()
        super(Blog, self).delete(*args, **kwargs)
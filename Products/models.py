from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from autoslug import AutoSlugField

# Create your models here.

class AllProduct(models.Model):
    product_title= models.CharField(max_length=100, unique=True)
    product_image= models.ImageField(upload_to="media", max_length=350, null=False, default=None)
    product_description=CKEditor5Field('Text', config_name='extends')
    new_price= models.IntegerField()
    old_price= models.IntegerField(null=True, blank=True,)
    product_tag= models.CharField(max_length=50, null=True, blank=True, default='View')
    product_slug= AutoSlugField(populate_from='product_title', unique=True, null=True, default=None)
    
    def save(self, *args, **kwargs):
        # Check if an image is already associated with this instance
        if self.pk:
            try:
                old_instance = AllProduct.objects.get(pk=self.pk)
                # Check if the image has changed
                if self.product_image and old_instance.product_image != self.product_image:
                    old_instance.product_image.delete()
            except AllProduct.DoesNotExist:
                pass  # Handle the case where the instance doesn't exist yet

        self.product_slug = None  # Set to None to trigger a new slug creation
        super(AllProduct, self).save(*args, **kwargs)
        
        if not self.old_price:
            self.old_price = self.new_price - 100
        super().save(*args, **kwargs)
    
    
    def delete(self, *args, **kwargs):
        self.product_image.delete()
        super(AllProduct, self).delete(*args, **kwargs)
  
        
class TopProduct(models.Model):
    product_title = models.CharField(max_length=100, unique=True)
    product_image = models.ImageField(upload_to="media", max_length=350, null=False, default=None)
    product_description = CKEditor5Field('Text', config_name='extends')
    new_price= models.IntegerField()
    old_price= models.IntegerField(null=True, blank=True,)
    product_tag = models.CharField(max_length=50, null=True, blank=True, default='View')
    product_slug = AutoSlugField(populate_from='product_title', unique=True, null=True, default=None)
    
    def save(self, *args, **kwargs):
        # Check if an image is already associated with this instance
        if self.pk:
            try:
                old_instance = TopProduct.objects.get(pk=self.pk)
                # Check if the image has changed
                if self.product_image and old_instance.product_image != self.product_image:
                    old_instance.product_image.delete()
            except TopProduct.DoesNotExist:
                pass  # Handle the case where the instance doesn't exist yet

        self.product_slug = None  # Set to None to trigger a new slug creation
        super(TopProduct, self).save(*args, **kwargs)
        
        if not self.old_price:
            self.old_price = self.new_price - 100
        super().save(*args, **kwargs)

  
    def delete(self, *args, **kwargs):
        # Delete the associated image when the instance is deleted
        self.product_image.delete()
        super(TopProduct, self).delete(*args, **kwargs)
       
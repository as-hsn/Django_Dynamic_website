# Generated by Django 5.0.2 on 2024-02-23 22:23

import autoslug.fields
import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_title', models.CharField(max_length=100, unique=True)),
                ('product_image', models.ImageField(default=None, max_length=350, upload_to='media')),
                ('product_description', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text')),
                ('new_price', models.IntegerField()),
                ('old_price', models.IntegerField(blank=True, null=True)),
                ('product_tag', models.CharField(blank=True, default='View', max_length=50, null=True)),
                ('product_slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='product_title', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TopProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_title', models.CharField(max_length=100, unique=True)),
                ('product_image', models.ImageField(default=None, max_length=350, upload_to='media')),
                ('product_description', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text')),
                ('new_price', models.IntegerField()),
                ('old_price', models.IntegerField(blank=True, null=True)),
                ('product_tag', models.CharField(blank=True, default='View', max_length=50, null=True)),
                ('product_slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='product_title', unique=True)),
            ],
        ),
    ]

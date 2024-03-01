# Generated by Django 5.0.1 on 2024-02-07 19:22

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_blog_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_slug',
            field=autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='blog_title', unique=True),
        ),
    ]
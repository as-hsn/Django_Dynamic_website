# Generated by Django 5.0.2 on 2024-02-12 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_blog_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
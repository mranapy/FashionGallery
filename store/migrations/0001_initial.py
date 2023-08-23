# Generated by Django 4.0 on 2023-08-10 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50, unique=True)),
                ('slug', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('cat_image', models.ImageField(blank=True, upload_to='photo/categories')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'categories',
            },
        ),
    ]

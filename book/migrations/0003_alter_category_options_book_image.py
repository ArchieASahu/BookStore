# Generated by Django 4.2.3 on 2023-07-15 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default='string', upload_to='book_images'),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.2.4 on 2021-11-26 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'категория', 'verbose_name_plural': 'категории'},
        ),
    ]
# Generated by Django 3.1 on 2021-12-28 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basketapp', '0003_alter_basket_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

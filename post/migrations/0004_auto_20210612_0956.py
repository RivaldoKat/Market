# Generated by Django 2.2.20 on 2021-06-12 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

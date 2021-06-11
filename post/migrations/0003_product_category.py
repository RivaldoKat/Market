# Generated by Django 3.2.4 on 2021-06-10 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_product_condition'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Fridge', 'Fridge'), ('Stove', 'Stove'), ('Laptop', 'Laptop'), ('Microoven', 'Microoven')], default='Fridge', max_length=50),
        ),
    ]

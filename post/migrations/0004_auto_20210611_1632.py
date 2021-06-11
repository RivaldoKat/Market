# Generated by Django 3.2.4 on 2021-06-11 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Fridge', 'Fridge'), ('Stove', 'Stove'), ('Laptop', 'Laptop'), ('Microoven', 'Microoven')], default='Fridge', max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
    ]

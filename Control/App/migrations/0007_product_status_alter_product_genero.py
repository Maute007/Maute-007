# Generated by Django 4.2 on 2023-07-07 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_rename_compras_product_entradas_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='genero',
            field=models.CharField(choices=[('M', 'M'), ('U', 'U'), ('F', 'F')], max_length=100, null=True),
        ),
    ]

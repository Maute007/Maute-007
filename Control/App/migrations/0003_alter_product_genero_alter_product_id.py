# Generated by Django 4.2 on 2023-07-07 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_alter_product_genero_alter_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='genero',
            field=models.CharField(choices=[('M', 'M'), ('F', 'F'), ('U', 'U')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

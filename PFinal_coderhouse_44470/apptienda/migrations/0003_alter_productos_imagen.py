# Generated by Django 4.1.3 on 2022-12-22 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptienda', '0002_alter_productos_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='imagen',
            field=models.ImageField(default='null', upload_to='productos', verbose_name='productos'),
        ),
    ]

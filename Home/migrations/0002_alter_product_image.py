# Generated by Django 4.0.4 on 2022-05-02 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='Home/media/photos'),
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-04 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_cart_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='caterogy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
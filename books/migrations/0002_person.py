# Generated by Django 4.2.7 on 2023-11-27 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя пользователя')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('register_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

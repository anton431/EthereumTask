# Generated by Django 4.1.7 on 2023-02-27 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_hash', models.CharField(blank=True, max_length=20, unique=True, verbose_name='Уникальный хеш')),
                ('tx_hash', models.CharField(blank=True, max_length=200, verbose_name='Xэш транзакции создания токена')),
                ('media_url', models.URLField(blank=True, verbose_name='url на изображение')),
                ('owner', models.CharField(blank=True, max_length=100, verbose_name='Адрес пользователя в сети Ethereum')),
            ],
        ),
    ]

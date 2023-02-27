from django.db import models


class Token(models.Model):
    unique_hash = models.CharField(max_length=20, unique=True, verbose_name='Уникальный хеш', blank=True) #возможно использовать UUIDField
    tx_hash = models.CharField(max_length=200, verbose_name='Xэш транзакции создания токена', blank=True)
    media_url = models.URLField(verbose_name='url на изображение', blank=True)
    owner = models.CharField(max_length=100, verbose_name='Адрес пользователя в сети Ethereum', blank=True)

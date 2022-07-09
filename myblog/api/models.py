import datetime
import uuid
from django.db import models


# Create your models here.
class Articles(models.Model):
    """記事のモデル"""

    class Meta:
        db_table = 'article'
        ordering = ['created_at']
        verbose_name = verbose_name_plural = '記事'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    title = models.CharField(verbose_name='タイトル', max_length=20, unique=True)
    text = models.TextField(verbose_name='本文', blank=False)
    img = models.ImageField(verbose_name='画像', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='登録日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)


class Genre(models.Model):
    """ジャンルのモデル"""
    class Meta:
        db_table = 'genre'
        ordering = ['id']
        verbose_name = verbose_name_plural = 'ジャンル'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    genre_name = models.CharField(verbose_name='ジャンル名', max_length=30, unique=True)
    articel = models.ForeignKey(
        Articles,
        verbose_name='記事',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )



from django.db import models


# Create your models here.
class Genre(models.Model):
    """ジャンルのモデル"""
    class Meta:
        db_table = 'genre'
        ordering = ['id']
        verbose_name = verbose_name_plural = 'ジャンル'

    genre_name = models.CharField(verbose_name='ジャンル名', max_length=30, unique=False)

    def __str__(self):
        return self.genre_name

class Articles(models.Model):
    """記事のモデル"""

    class Meta:
        db_table = 'article'
        ordering = ['created_at']
        verbose_name = verbose_name_plural = '記事'

    title = models.CharField(verbose_name='タイトル', max_length=20, unique=True,)
    text = models.TextField(verbose_name='本文', blank=False)
    img = models.ImageField(verbose_name='画像', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='登録日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    genre = models.ForeignKey(
        Genre,
        verbose_name='ジャンル',
        on_delete=models.PROTECT,
        null=True,
        blank=True,

    )

    def __str__(self):
        return self.title





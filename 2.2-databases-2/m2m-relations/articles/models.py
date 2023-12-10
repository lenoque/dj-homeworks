from django.db import models
from django.db.models import Q, UniqueConstraint


class Tag(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')

    def __str__(self):
        return self.name


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Scope(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, related_name='scopes', on_delete=models.CASCADE)
    is_main = models.BooleanField(default=False)

    constraints = [
        UniqueConstraint(fields=['tag'], condition=Q(is_main=True), name='unique_tag_main')
    ]

    class Meta:
        unique_together = ('tag', 'article')

    def __str__(self):
        return f'{self.article} {self.tag}'

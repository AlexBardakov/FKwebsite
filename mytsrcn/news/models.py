from django.db import models


class News(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Новость')
    published = models.DateTimeField(verbose_name='Дата публикации', )
    author = models.CharField(max_length=20, verbose_name='Автор', blank=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ('-published',)

    def __str__(self):
        return '{}. {}... {}... {}'.format(self.title, self.text[:10],
                                           self.published, self.author)

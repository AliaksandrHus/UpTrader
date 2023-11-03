from django.db import models


class Menu(models.Model):
    name = models.CharField('Название', max_length=100)
    url = models.CharField('Ссылка', blank=True, max_length=255)
    position = models.PositiveIntegerField('Позиция', default=1)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('position',)
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

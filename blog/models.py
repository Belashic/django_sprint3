from django.db import models
from django.contrib.auth import get_user_model
import datetime


class BaseModel(models.Model):
    is_published=models.BooleanField(
        default=True, 
        verbose_name = 'Опубликовано',
        help_text = 'Снимите галочку, чтобы скрыть публикацию.'
    )
    created_at = models.DateTimeField(
        'Добавлено',
        auto_now_add=True
    )


    class Meta:
        abstract = True
# Create your models here.


User = get_user_model()


class Category(BaseModel):
    title = models.CharField(
        'Заголовок',
        max_length=256,
        blank=False)
    description = models.TextField(
        'Описание',
        blank=False)
    slug = models.SlugField(
        'Идентификатор',
        unique=True,
        blank=False,
        help_text='Идентификатор страницы для URL; разрешены символы '
        'латиницы, цифры, дефис и подчёркивание.')

    def str(self):
        return self.title

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'


class Location(BaseModel):
    name = models.CharField(
        'Название места',
        max_length=256,
        blank=False)

    def str(self):
        return self.name

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'


class Post(BaseModel):
    title = models.CharField(
        'Заголовок',
        max_length=256,
        blank=False)
    text = models.TextField(
        'Текст',
        blank=False)
    pub_date = models.DateTimeField(
        'Дата и время публикации',
        default=datetime.datetime.now,
        blank=False,
        help_text='Если установить дату и время в будущем'
        ' — можно делать отложенные публикации.')
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        related_name='location',
        verbose_name='Местоположение',
        null=True,
        blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='category',
        verbose_name='Категория',
        null=True,
        blank=False)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='author',
        verbose_name='Автор публикации',
        blank=False)

    def str(self):
        return self.title
    
    
    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        ordering = ['-pub_date']
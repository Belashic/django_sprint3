'''
from django.db import models
import datetime

# Create your models here.
class BaseModel(models.Model):
    is_published=models.BooleanField(
        default=True, 
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )
    created_at = models.DateTimeField(
        'Добвылено',
        avto_now_add=True)
    
    class Meta:
        abstract = True
'''
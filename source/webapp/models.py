from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models


STATUS_CHOICES = [
    ('all', 'Публичный'),
    ('private', 'Приватный'),
]


class Album(models.Model):
    name = models.CharField(max_length=2000, verbose_name='Название')
    description = models.CharField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    author = models.ForeignKey(get_user_model(), verbose_name='Автор', related_name='author_album',
                               on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')


class Photo(models.Model):
    photo_img = models.ImageField(upload_to='photos', verbose_name='Картинка')
    signature = models.CharField(max_length=2000, verbose_name='Подпись')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    author = models.ForeignKey(get_user_model(), verbose_name='Автор', related_name='author_photos',
                               on_delete=models.CASCADE)
    album = models.ForeignKey(Album, null=True, blank=True, verbose_name='Альбом', related_name='photo_album',
                              on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='all', verbose_name='Публичный')

    def is_in_favorite(self, user):
        liked_by_user = self.favorite_photo.filter(author=user)
        if liked_by_user.count() > 0:
            return True
        else:
            return False


class Favorite(models.Model):
    photo = models.ForeignKey(Photo,  verbose_name='Фото', related_name='favorite_photo', on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), related_name='author_favorites',
                               verbose_name='Автор', on_delete=models.CASCADE)


class Jopening(models.Model):
    name = models.CharField(max_length=500, verbose_name='Оглавление')
    description = models.CharField(max_length=6000, null=True, blank=True, verbose_name='Описание')
    author = models.ForeignKey(get_user_model(), verbose_name='Автор', related_name='jopenings_album',
                               on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')


class Messages(models.Model):
    sender: AbstractUser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                                             related_name='messages_sender', verbose_name='Пользователь')
    reciver = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                                related_name='messages_reciver', verbose_name='Пользователь')
    message_text = models.TextField(max_length=400, verbose_name='Текст сообщения')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return str(self.pk) + "'s message"

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

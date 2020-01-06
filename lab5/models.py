# coding=utf-8
from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):

    # Название товара
    name = models.CharField(max_length=255)

    # Описание товара
    description = models.CharField(max_length=1000)

    # Продавец
    seller = models.CharField(max_length=255)

    # Короткое описание товара
    def short_description(self):
        return self.description[:126]

    def __str__(self):
        return ' '.join([
            self.name,
            ' from ',
            self.seller,
        ])


class Review(models.Model):

    # Пользователь, который оставил отзыв
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Товар, под которым оставлен отзыв
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    # Текст отзыва
    description = models.CharField(
        max_length=500,
    )

    def __str__(self):
        return ' '.join([
            'review \'',
            str(self.description),
            ' \' from user @',
            str(self.user.username),
        ])


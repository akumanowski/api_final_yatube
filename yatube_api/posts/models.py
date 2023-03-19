"""Проект спринта 9: модуль управления моделями приложения Post."""
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    """Класс управления данными группы."""
    title = models.CharField(max_length=200,
                             verbose_name='Наименование',
                             help_text='Cформулируйте наименование группы')
    slug = models.SlugField(unique=True,
                            verbose_name='Тег',
                            help_text='Присвойте группе уникальный тег')
    description = models.TextField(verbose_name='Описание',
                                   help_text='Опишите группу. '
                                             'Её цели и задачи')

    def __str__(self):
        return self.title


class Post(models.Model):
    """Класс управления данными постов."""
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='posts',
        verbose_name='Группа',
        help_text='Выберите группу, к которой отностится пост'
    )

    class Meta:
        default_related_name = 'posts'
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.text[15]


class Comment(models.Model):
    """Класс управления данными комментариев к постам."""
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)
        default_related_name = 'comments'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text[:15]


class Follow(models.Model):
    """Класс управления подписками."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик',
        help_text='Укажите подписчика'
    )

    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор постов',
        help_text='Укажите автора постов'
    )

    class Meta:
        constraints = [models.UniqueConstraint(fields=('user', 'following'),
                                               name='unique_subscribe')]
        default_related_name = 'follows'
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return f"Подписка {self.following.username} на {self.user.username}"

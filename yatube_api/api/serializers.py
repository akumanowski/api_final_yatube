"""Проект спринта 9: модуль сериалайзер приложения Api."""
import base64

from django.core.files.base import ContentFile
from django.shortcuts import get_object_or_404
from posts.models import Comment, Follow, Group, Post, User
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]

            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        return super().to_internal_value(data)


class GroupSerializer(serializers.ModelSerializer):
    """Класс-сериализатор для Group."""

    class Meta:
        model = Group
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    """Класс-сериализатор для Post."""
    author = SlugRelatedField(slug_field='username', read_only=True)
    image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        fields = '__all__'
        model = Post
        read_only_fields = ('id', 'pub_date', 'author',)


class CommentSerializer(serializers.ModelSerializer):
    """Класс-сериализатор для Comment."""
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username')
    post = serializers.SlugRelatedField(read_only=True, slug_field='id')

    class Meta:
        model = Comment
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    """Класс-сериализатор для Follow."""
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        # read_only=True,
        slug_field='username',
        queryset=User.objects.all()
    )
    # following = serializers.CharField(source='following.username')

    class Meta:
        model = Follow
        fields = ('user', 'following')

    def validate_following(self, value):
        following = value
        # get_object_or_404(User, username=value)
        if following == self.context['request'].user:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя!'
            )
        return following

    # def validate(self, data):
    #     if self.context['request'].user == data['following']:
    #         raise serializers.ValidationError(
    #             'Нельзя подписаться на самого себя!')
    #     return data

    # def create(self, validated_data):
    #     user = self.context['request'].user
    #     following = get_object_or_404(User,
    #                                   username=validated_data.get(
    #                                       'following'
    #                                   )
    #                                   )
    #     follow = Follow.objects.create(user=user, following=following)
    #     return follow

    # def create(self, validated_data):
    #     return Follow.objects.create(**validated_data)

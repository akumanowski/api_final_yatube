"""Проект спринта 9: модуль контроллер приложения Api."""
from django.shortcuts import get_object_or_404
from posts.models import Group, Post
from rest_framework import filters, permissions
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .permissions import AuthorPermission
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)


class GroupViewSet(ReadOnlyModelViewSet):
    """Классы-вьюсет для Group."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PostViewSet(ModelViewSet):
    """Классы-вьюсет для Post."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorPermission,
                          permissions.IsAuthenticatedOrReadOnly)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(ModelViewSet):
    """Классы-вьюсет для Comment."""
    serializer_class = CommentSerializer
    permission_classes = (AuthorPermission,
                          permissions.IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user, post=post)

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, id=post_id)
        new_queryset = post.comments
        return new_queryset


class FollowViewSet(ModelViewSet):
    """Классы-вьюсет для Follow."""
    http_method_names = ('get', 'post',)
    serializer_class = FollowSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user__username', 'following__username')

    def perform_create(self, serializer):
        return serializer.save(
            user=self.request.user
        )

    def get_queryset(self):
        return self.request.user.follower.all()

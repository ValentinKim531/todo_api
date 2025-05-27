from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import ValidationError
from .models import Task
from .serializers import TaskSerializer
import logging

logger = logging.getLogger(__name__)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["completed"]
    search_fields = ["title"]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Task.objects.filter(user=user).order_by("-created_at")
        return Task.objects.none()

    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user)
        except Exception as e:
            logger.error(f"Ошибка при сохранении задачи: {e}")
            raise ValidationError("Ошибка при сохранении задачи.")

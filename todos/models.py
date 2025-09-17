from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Todo(models.Model):
    title = models.CharField(max_length=100, verbose_name="할일", blank=False)
    is_completed = models.BooleanField(default=False, verbose_name="완료여부")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성일시")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정일시")
    due_date = models.DateField(verbose_name="마감기한")
    user = models.ForeignKey(
        User,
        related_name="todo",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="작성자",
    )

    def __str__(self):
        return self.title

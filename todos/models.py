from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=200, verbose_name="할일")
    is_completed = models.BooleanField(default=False, verbose_name="완료여부")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성일시")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정일시")

    def __str__(self):
        return self.title

from django.db import models
from django.core.validators import MinLengthValidator

class Todo(models.Model):
    title = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(3, "Title must be at least 3 characters long")]
    )
    description = models.TextField(
        blank=True,
        help_text="Add any additional details about the task"
    )
    completed = models.BooleanField(
        default=False,
        help_text="Mark if the task is completed"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} {'✓' if self.completed else '○'}"

    def get_status_display(self):
        return "Completed" if self.completed else "Pending"

    def is_recently_created(self):
        from django.utils import timezone
        return (timezone.now() - self.created_at).days < 1

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

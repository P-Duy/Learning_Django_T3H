from django.db import models


# Create your models here.
class PostModel(models.Model):
    title = models.CharField(max_length=100, null=False)
    summary = models.CharField(max_length=500, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

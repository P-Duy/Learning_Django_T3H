from django.db import models
import os


# Create your models here.
class PostModel(models.Model):
    title = models.CharField(max_length=100, null=False)
    summary = models.CharField(max_length=500, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rank = models.IntegerField(null=True)
    image = models.ImageField(null=True, upload_to="images")
    file = models.FileField(upload_to="files", null=True)

    def __str__(self):
        return self.title

    def get_file_name(self):
        return os.path.basename(self.file.url)

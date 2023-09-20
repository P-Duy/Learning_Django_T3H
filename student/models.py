from django.db import models


# Create your models here.
class Student(models.Model):
    ho = models.CharField(max_length=20, null=False)
    ten = models.CharField(max_length=255, null=False)
    ngay_sinh = models.DateField()
    dia_chi = models.TextField()
    diem_toan = models.IntegerField()
    diem_van = models.IntegerField()
    diem_anh = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ten

    def get_title(self):
        return self.ho + " " + self.ten

from django.db import models
from students.models import Student

class StudentDetail(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.student.name} Detail"

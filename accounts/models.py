from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class Account(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=100, unique=True)

    my_courses = models.ManyToManyField(
        "courses.Course",
        related_name="students",
        through="students_courses.StudentCourse",
    )
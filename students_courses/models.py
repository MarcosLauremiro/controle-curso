from django.db import models
import uuid

from django.forms import CharField


class StudentCourseStatus(models.TextChoices):
    PENDING = "pending"
    ACCEPTED = "accepted"
    

class StudentCourse(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(
        choices=StudentCourseStatus.choices, default=StudentCourseStatus.PENDING
    )
    course = models.ForeignKey(
        "courses.Course", related_name="students_courses", on_delete=models.CASCADE
    )
    student = models.ForeignKey(
        "accounts.Account", related_name="students_courses", on_delete=models.CASCADE
    )

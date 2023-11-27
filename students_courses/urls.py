from django.urls import path
from .views import StudentCourseView


urlpatterns = [
    path("courses/<uuid:course_id>/students/", StudentCourseView.as_view()),
]
from django.urls import path
from .views import CourseView, CourseDatailView


urlpatterns = [
    path("courses/", CourseView.as_view()),
    path("courses/<uuid:course_id>/", CourseDatailView.as_view()),
]

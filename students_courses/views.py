from rest_framework.generics import RetrieveUpdateAPIView
from courses.models import Course
from courses.serializers import RegisterCourserSerializer


class StudentCourseView(RetrieveUpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = RegisterCourserSerializer
    lookup_url_kwarg = "course_id"
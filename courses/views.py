from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Course
from .serializers import CourseSerializer
from .permissions import InstructorReadOnlyPermission
from rest_framework.permissions import IsAuthenticated


class CourseView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [InstructorReadOnlyPermission]

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_serializer_class(self):
        if self.request.method == "GET":
            return CourseSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            queryset = Course.objects.all()
        else:
            queryset = Course.objects.filter(students=user)

        return queryset


class CourseDatailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, InstructorReadOnlyPermission]

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_url_kwarg = "course_id"

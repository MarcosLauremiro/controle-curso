from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import NotFound
from .permissions import InstructorPermission, InstructorReadOnlyPermission
from rest_framework.permissions import IsAuthenticated
from .serializers import ContentSerializer
from courses.models import Course
from .models import Content


class ContentsView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [InstructorPermission]

    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_url_kwarg = "course_id"

    def perform_create(self, serializer):
        course = Course.objects.get(id=self.kwargs["course_id"])
        if not course:
            raise NotFound({"detail": "course not found."})
        serializer.save(course=course)


class ContentDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, InstructorReadOnlyPermission]

    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_url_kwarg = "course_id"

    def get_object(self):
        try:
            course_id = self.kwargs["course_id"]
            content_id = self.kwargs["content_id"]
            Course.objects.get(id=course_id)
            content = Content.objects.get(id=content_id)

        except Content.DoesNotExist:
            raise NotFound({"detail": "content not found."})
        except Course.DoesNotExist:
            raise NotFound({"detail": "course not found."})
        
        self.check_object_permissions(self.request, content)
        return content

from django.urls import path
from .views import ContentsView, ContentDetailView


urlpatterns = [
    path("courses/<uuid:course_id>/contents/", ContentsView.as_view()),
    path(
        "courses/<uuid:course_id>/contents/<uuid:content_id>/",
        ContentDetailView.as_view(),
    ),
]

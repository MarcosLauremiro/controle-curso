from django.urls import path
from .views import AccountsView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('login/', jwt_views.TokenObtainPairView.as_view()),
    path('accounts/', AccountsView.as_view()),
]
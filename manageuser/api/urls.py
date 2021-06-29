from django.urls import path
from .views import UserCreateAPIView, UserCurrent, testing

urlpatterns = [
    path('test', testing.as_view()),
    path('currentuser', UserCurrent.as_view()),
    path('createuser', UserCreateAPIView.as_view()),
]
from django.urls import path
from posts.views import PostAPIView


urlpatterns = [
    path('api/posts/', PostAPIView.as_view()),
    path('api/posts/<int:pk>/', PostAPIView.as_view())
]

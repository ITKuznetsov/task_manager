from django.urls import include, path

from tasks.views import TaskAPIView

urlpatterns = [
    path('task', TaskAPIView.as_view()),
]

from rest_framework import generics
from django.shortcuts import render

from tasks.models import Task
from tasks.serializers import TaskSerializer


class TaskAPIView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

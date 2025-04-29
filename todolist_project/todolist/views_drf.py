from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.contrib.auth.models import User

from .models import Task
from .serializers import TaskSerializer, UserSerializer
from django.db.models import Q

# --- TASK CRUD ---

class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        search_query = self.request.query_params.get('q', '')

        if search_query:
            return Task.objects.filter(
                Q(title__icontains=search_query) & ~Q(user=self.request.user)
            )
        return Task.objects.exclude(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MyTaskListView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        task = self.get_object()
        if task.user != self.request.user:
            raise PermissionDenied("You cannot edit this task.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.user != self.request.user:
            raise PermissionDenied("You cannot delete this task.")
        instance.delete()


# --- DETAIL API ---
class TaskDetailJsonView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        task = generics.get_object_or_404(Task, pk=pk)
        data = {
            'title': task.title,
            'completed': task.completed,
            'creator': task.user.username,
        }
        return Response(data)


# --- USER REGISTER ---
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

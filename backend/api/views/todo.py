from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import *
from rest_framework import viewsets
from api.serializers import TodoSerializer

from django.http import JsonResponse

class TodoList(APIView):
    def get(self, request, format=None):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True, context={'request': request})
        return Response(serializer.data)

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

def list_todos(request, format=None):
    all_todos = list(Todo.objects.values())
    return JsonResponse(all_todos, safe=False)
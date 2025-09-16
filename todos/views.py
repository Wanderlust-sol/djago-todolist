from todos.models import Todo

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer

class TodoList(APIView):
  class TodoSerializer(ModelSerializer):
    class Meta:
      model = Todo
      fields = [
        "id",
        "title",
        "is_completed",
        "created_at",
        "updated_at"
      ]

  def get(self, request):
    todos = Todo.objects.all()
    serializer = self.TodoSerializer(todos, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
class TodoCreate(APIView):
  class TodoSerializer(ModelSerializer):
    class Meta:
      model = Todo
      fields = [
        "title",
      ]
    
  def post(self, request):
    serializer = self.TodoSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    Todo.objects.create(
      title=serializer.validated_data["title"],
    )
    return Response(status=status.HTTP_201_CREATED)
from todos.models import Todo
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.utils import timezone

class TodoList(APIView):
  class TodoSerializer(ModelSerializer):
    class Meta:
      model = Todo
      fields = [
        "id",
        "title",
        "is_completed",
        "created_at",
        "updated_at",
        "due_date",
        "user"
      ]

  def get(self, request):
    todos = Todo.objects.all()
    serializer = self.TodoSerializer(todos, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
class TodoCreate(APIView):
  class TodoSerializer(ModelSerializer):
    is_completed = serializers.BooleanField(required=False)
    user_email = serializers.EmailField()
    due_date = serializers.DateField(required=False)
    class Meta:
      model = Todo
      fields = [
        "title",
        "is_completed",
        "user_email",
        "due_date"
      ]
    
  def post(self, request):
    serializer = self.TodoSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    try:
      user = User.objects.get(email=serializer.validated_data["user_email"])
    except User.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
      return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    Todo.objects.create(
      title=serializer.validated_data["title"],
      is_completed=serializer.validated_data.get("is_completed", False),
      user=user,
      due_date=serializer.validated_data.get("due_date", timezone.now())
    )
    return Response(status=status.HTTP_201_CREATED)
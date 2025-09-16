from django.urls import path
from todos import views


urlpatterns = [path("list/", views.TodoList.as_view()), path('create/', views.TodoCreate.as_view())]

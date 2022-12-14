from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserListCreateAPIView.as_view(), name="user"),
    path('questions/', views.QuestionListCreateAPIView.as_view(), name="question"),
    path('questions/<int:pk>/update', views.QuestionUpdateDeleteAPIView.as_view(), name="question"),
    path('choice/', views.ChoiceListCreateAPIView.as_view(), name="choice"),
    path('choice/<int:pk>/update', views.ChoiceUpdateDeleteAPIView.as_view(), name="choice"),
]
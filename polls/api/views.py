from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication

from .serializers import QuestionSerializer, ChoiceSerializer, UserSerializer
from .permissions import IsAuthor
from polls.models import Question, Choice


class QuestionListCreateAPIView(ListCreateAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]


class QuestionUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthor]
    authentication_classes = [TokenAuthentication]


class ChoiceListCreateAPIView(ListCreateAPIView):
    serializer_class = ChoiceSerializer
    queryset = Choice.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]


class ChoiceUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ChoiceSerializer
    queryset = Choice.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]


class UserListCreateAPIView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

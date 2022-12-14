from django.contrib.auth.models import User
from rest_framework import serializers

from polls.models import Question, Choice


class QuestionChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = (
            'choice_text', 'votes'
        )


class QuestionSerializer(serializers.ModelSerializer):
    choice = QuestionChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['author', 'question_text', 'pub_date', 'choice']


class ChoiceSerializer(serializers.ModelSerializer):
    votes = serializers.ReadOnlyField()

    class Meta:
        model = Choice
        fields = ['question', 'choice_text', 'votes']


class UserSerializer(serializers.ModelSerializer):
    question = QuestionSerializer

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

    # def create(self, validated_data):
    #     del validated_data['question']
    #     author = User.objects.create(**validated_data)
    #     # for question in questions:
    #     #     Question.objects.create(author=author, **question)
    #     return author




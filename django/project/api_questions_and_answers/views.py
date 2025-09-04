from rest_framework import generics
from rest_framework.exceptions import NotFound
from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer


# Questions
class QuestionListCreateView(generics.ListCreateAPIView):
    """Список всех вопросов и создание нового вопроса."""

    queryset = Question.objects.all().order_by("-created_at")
    serializer_class = QuestionSerializer
    http_method_names = ["get", "post"]


class QuestionRetrieveDeleteView(generics.RetrieveDestroyAPIView):
    """Получение и удаление вопроса по ID."""

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    http_method_names = ["get", "delete"]


# Answers
class AnswerCreateView(generics.CreateAPIView):
    """Создание ответа на вопрос по ID."""

    serializer_class = AnswerSerializer
    http_method_names = ["post"]

    def perform_create(self, serializer):
        question_id = self.kwargs["question_id"]
        try:
            question = Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            raise NotFound("Вопрос не найден")
        serializer.save(question=question)


class AnswerRetrieveDeleteView(generics.RetrieveDestroyAPIView):
    """Получение и удаление ответа по ID."""

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    http_method_names = ["get", "delete"]

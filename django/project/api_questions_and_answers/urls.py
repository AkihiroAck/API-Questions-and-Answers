from django.urls import path
from .views import QuestionListCreateView, QuestionRetrieveDeleteView, AnswerCreateView, AnswerRetrieveDeleteView


urlpatterns = [
    # Questions
    path("questions/", QuestionListCreateView.as_view(), name="question-list-create"),
    path("questions/<int:pk>/", QuestionRetrieveDeleteView.as_view(), name="question-detail"),

    # Answers
    path("questions/<int:question_id>/answers/", AnswerCreateView.as_view(), name="answer-create"),
    path("answers/<int:pk>/", AnswerRetrieveDeleteView.as_view(), name="answer-detail"),
]

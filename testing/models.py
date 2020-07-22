from django.db import models
from test_constructor.models import Test, Question, Option


class TestResult(models.Model):
    test = models.ForeignKey(Test, default=None, on_delete=models.CASCADE, null=True)
    user = models.CharField(max_length=100, default="Неизвестный")
    amount_of_points = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Результат теста'
        verbose_name_plural = 'Результаты тестов'


class QuestionResult(models.Model):
    test_result = models.ForeignKey(TestResult, default=None, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, default=None, on_delete=models.CASCADE, null=True)
    text_answer = models.CharField(max_length=200, default="", null=True, blank=True)
    amount_of_points = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Результат вопроса'
        verbose_name_plural = 'Результаты вопросов'


class OptionResult(models.Model):
    question_result = models.ForeignKey(QuestionResult, default=None, on_delete=models.CASCADE, null=True)
    option = models.ForeignKey(Option, default=None, on_delete=models.CASCADE, null=True)
    is_selected = models.BooleanField()

    class Meta:
        verbose_name = 'Результат варианта'
        verbose_name_plural = 'Результаты вариантов'

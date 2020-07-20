from django.db import models


class TestResult(models.Model):
    test_code = models.IntegerField(default=10000000)
    user = models.CharField(max_length=100, default="Неизвестный")

    class Meta:
        verbose_name = 'Результат теста'
        verbose_name_plural = 'Результаты тестов'


class QuestionResult(models.Model):
    test_result = models.ForeignKey(TestResult, default=None, on_delete=models.CASCADE, null=True)
    question_id = models.IntegerField(default=0)
    text_answer = models.CharField(max_length=200, default="")

    class Meta:
        verbose_name = 'Результат вопроса'
        verbose_name_plural = 'Результаты вопросов'


class OptionResult(models.Model):
    question_result = models.ForeignKey(QuestionResult, default=None, on_delete=models.CASCADE, null=True)
    is_selected = models.BooleanField()

    class Meta:
        verbose_name = 'Результат варианта'
        verbose_name_plural = 'Результаты вариантов'

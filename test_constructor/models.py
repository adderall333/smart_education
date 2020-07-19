from django.db import models
from django.contrib.auth.models import User


class Test(models.Model):
    title = models.CharField(max_length=100, default="")
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE, null=True)
    pub_date = models.DateTimeField()
    code = models.IntegerField(default=10000000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class Question(models.Model):
    test_code = models.IntegerField(default=10000000)
    text = models.TextField()
    image = models.ImageField()
    amount_of_points = models.IntegerField(default=1)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=100, default="")
    is_correct = models.BooleanField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'

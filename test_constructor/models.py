from django.db import models
from django.contrib.auth.models import User


class Test(models.Model):
    title = models.CharField(max_length=100, default="")
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE, null=True)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class Question(models.Model):
    test_title = models.CharField(max_length=100, default="")
    text = models.TextField()
    image = models.ImageField()


class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=100, default="")
    is_correct = models.BooleanField()


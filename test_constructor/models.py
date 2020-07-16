from django.db import models
from django import forms
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
    options_count = models.IntegerField(default=0)
    text = models.TextField()
    image = models.ImageField()
    options = models.TextField()
    correct_answer = models.CharField(max_length=100, default="")


class TestForm(forms.Form):
    title = forms.CharField(label="Название теста")


class QuestionForm(forms.Form):
    options_count = forms.IntegerField(label="Количество вариантов ответа")
    text = forms.CharField(widget=forms.Textarea, label="Текст вопроса")
    image = forms.ImageField(label="Картинка", required=False)
    options = forms.CharField(widget=forms.Textarea, label="Варианты ответа", required=False)
    correct_answer = forms.CharField(max_length=100, initial="", label="Правильный ответ")

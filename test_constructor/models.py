from django.db import models
from django import forms


class Test(models.Model):
    title = models.CharField(max_length=100, default="")
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    with_options = models.BooleanField()
    text = models.TextField()
    image = models.ImageField()
    options = models.TextField()
    correct_answer = models.CharField(max_length=100, default="")


QUESTION_TYPES = (
    ("1", "Вопрос с одним вариантом ответа"),
    ("2", "Вопрос с несколькими вариантами ответа"),
    ("3", "Вопрос с текстовым ответом")
)


class TestForm(forms.Form):
    title = forms.CharField(label="Название теста")


class QuestionForm(forms.Form):
    type = forms.ChoiceField(choices=QUESTION_TYPES, label="Тип вопроса")
    text = forms.CharField(widget=forms.Textarea, label="Текст вопроса")
    image = forms.ImageField(label="Картинка")
    options = forms.CharField(widget=forms.Textarea, label="Варианты ответа")
    correct_answer = forms.CharField(max_length=100, initial="", label="Правильный ответ")
from django.db import models


class Test(models.Model):
    test_title = models.CharField('название теста', max_length = 100)
    pub_date = models.DateTimeField('дата публикации')

    def __str__ (self):
        return self.test_title

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'

class Question(models.Model):
    test = models.ForeignKey(Test, on_delete = models.CASCADE)
    with_options = models.BooleanField('тип вопроса')
    text = models.TextField('текст вопроса')
    image = models.ImageField('картинка')
    options = models.TextField('варианты ответа')
    correct_answers = models.TextField('правильные ответы')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

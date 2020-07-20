# Generated by Django 3.0.8 on 2020-07-20 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_code', models.IntegerField(default=10000000)),
                ('user', models.CharField(default='Неизвестный', max_length=100)),
            ],
            options={
                'verbose_name': 'Результат теста',
                'verbose_name_plural': 'Результаты тестов',
            },
        ),
        migrations.CreateModel(
            name='QuestionResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_id', models.IntegerField(default=0)),
                ('text_answer', models.CharField(default='', max_length=200)),
                ('test_result', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='testing.TestResult')),
            ],
            options={
                'verbose_name': 'Результат вопроса',
                'verbose_name_plural': 'Результаты вопросов',
            },
        ),
        migrations.CreateModel(
            name='OptionResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_selected', models.BooleanField()),
                ('question_result', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='testing.QuestionResult')),
            ],
            options={
                'verbose_name': 'Результат варианта',
                'verbose_name_plural': 'Результаты вариантов',
            },
        ),
    ]
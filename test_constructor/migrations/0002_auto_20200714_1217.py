# Generated by Django 3.0.8 on 2020-07-14 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_constructor', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={},
        ),
        migrations.RemoveField(
            model_name='question',
            name='correct_answers',
        ),
        migrations.RemoveField(
            model_name='test',
            name='test_title',
        ),
        migrations.AddField(
            model_name='question',
            name='correct_answer',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='test',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='question',
            name='options',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='with_options',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='test',
            name='pub_date',
            field=models.DateTimeField(),
        ),
    ]

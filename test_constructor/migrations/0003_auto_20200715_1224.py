# Generated by Django 3.0.8 on 2020-07-15 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_constructor', '0002_auto_20200714_1217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='test',
        ),
        migrations.RemoveField(
            model_name='question',
            name='with_options',
        ),
        migrations.AddField(
            model_name='question',
            name='options_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='test_title',
            field=models.CharField(default='', max_length=100),
        ),
    ]
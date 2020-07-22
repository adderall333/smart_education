from django.contrib import admin
from .models import TestResult, QuestionResult, OptionResult


admin.site.register(TestResult)
admin.site.register(QuestionResult)
admin.site.register(OptionResult)

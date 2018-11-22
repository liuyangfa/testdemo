# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)
# @admin.site.register(Question)
# class QuestionAdmin(admin.ModelAdmin):
#     list_display = ('question_text', 'pub_date')
#
#
# @admin.site.register(Choice)
# class ChoiceAdmin(admin.ModelAdmin):
#     list_display = ('question', 'choice_text', 'votes')

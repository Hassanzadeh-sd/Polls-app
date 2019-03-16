from django.contrib import admin
from . import models

class QuestionInlines(admin.TabularInline):
    model=  models.Choice
    extra=  2

@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display=   ('text',)
    inlines=        [QuestionInlines]

@admin.register(models.Choice)
class Choice(admin.ModelAdmin):
    list_display=   ('text','vote','display_question')

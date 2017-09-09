from django.contrib import admin
from Degree360 import models

admin.site.register(models.Survey)
admin.site.register(models.RelationType)
admin.site.register(models.FeedbackProvider)
admin.site.register(models.QuestionSection)
admin.site.register(models.Question)
admin.site.register(models.MultiChoiceAnswer)
admin.site.register(models.OpenAnswer)
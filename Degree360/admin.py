from django.contrib import admin
from Degree360.models import RelationType, FeedbackProvider, Survey

# Register your models here.
admin.site.register(Survey)
admin.site.register(RelationType)
admin.site.register(FeedbackProvider)
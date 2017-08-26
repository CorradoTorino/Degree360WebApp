from django.db import models
    
class RelationType(models.Model):
    relation_type = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    
class FeedbackProvider(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    relation_type = models.ForeignKey(RelationType, on_delete=models.CASCADE)


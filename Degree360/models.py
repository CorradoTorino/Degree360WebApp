from django.db import models
    
class RelationType(models.Model):
    relation_type = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return '{}: {}'.format(self.relation_type, self.description) 
    
class FeedbackProvider(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    relation_type = models.ForeignKey(RelationType, on_delete=models.CASCADE)
    
    def __str__(self):
        return '{} {} ({})'.format(self.name, self.last_name, self.email) 



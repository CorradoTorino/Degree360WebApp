from django.db import models

import uuid
    
class Survey(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employee_name = models.CharField(max_length=100, blank=True, default='')
    employee_last_name = models.CharField(max_length=100, blank=True, default='')
    employee_email = models.EmailField(max_length=100)
    
    @classmethod
    def create(cls, name, lastName, email):
        instance = cls(employee_name=name, employee_last_name=lastName, employee_email=email)
        instance.save()
        return instance
        
    def __str__(self):
        return '{} {}'.format(self.employee_name, self.employee_last_name)
    
    
class RelationType(models.Model):
    relation_type = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    
    @classmethod
    def create(cls, relation_type, description, survey):
        instance = cls(relation_type=relation_type, description=description, survey=survey)
        instance.save()
        return instance
    
    def __str__(self):
        return '{}'.format(self.relation_type, self.description) 
    
class FeedbackProvider(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, default='')
    email = models.EmailField(max_length=100)
    relation_type = models.ForeignKey(RelationType, on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
        
    @classmethod
    def create(cls, name, last_name, email, relation_type, survey):
        instance = cls(name=name, last_name=last_name, email=email, relation_type=relation_type, survey=survey)
        instance.save()
        return instance
    
    def __str__(self):
        return '{} {} ({})'.format(self.name, self.last_name, self.email)
    
    class Meta:
        unique_together = (("survey", "email"),)



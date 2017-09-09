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

class QuestionSection(models.Model):
    description = models.CharField(max_length=100)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.description
    
class Question(models.Model):
    text = models.CharField(max_length=200)
    section = models.ForeignKey(QuestionSection, on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(self.section, self.text)
    
class MultiChoiceAnswer(models.Model):
    feedback_provider = models.ForeignKey(FeedbackProvider, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    
    NEVER = 0
    RARELY = 1
    SOMETIMES = 2
    OFTEN = 3
    ALWAYS = 4

    ANSWER_CHOICES = (
        (NEVER, 'Never'),
        (RARELY, 'Rarely'),
        (SOMETIMES, 'Sometimes'),
        (OFTEN, 'Often'),
        (ALWAYS, 'Always'),
    )
    
    answer = models.IntegerField( choices=ANSWER_CHOICES, default=NEVER)
    
    def __str__(self):
        return '{} {}'.format(self.question, self.ANSWER_CHOICES[self.answer][1])
    
class OpenAnswer(models.Model):
    feedback_provider = models.ForeignKey(FeedbackProvider, on_delete=models.CASCADE)    
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=1000, blank=True, default='')
    
    def __str__(self):
        return '{}...'.format(self.answer[0:50])
    

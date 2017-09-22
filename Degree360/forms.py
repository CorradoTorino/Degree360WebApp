
from django.forms import ModelForm, BaseModelFormSet



from Degree360.models import FeedbackProvider, MultiChoiceAnswer

class FeedbackProviderForm(ModelForm):
    class Meta:
        model = FeedbackProvider
        fields = ['name', 'last_name', 'email', 'relation_type']

class MultiChoiceAnswerForm(ModelForm):
    
    class Meta:
        model = MultiChoiceAnswer
        fields = ['answer']
        
class MultiChoiceAnswerFormSet(BaseModelFormSet):
    
    def __init__(self, *args, **kwargs):
        super(MultiChoiceAnswerFormSet, self).__init__(*args, **kwargs)
        #self.queryset = MultiChoiceAnswer.objects.all()
    
    class Meta:
        model = MultiChoiceAnswer
        fields = ['answer']
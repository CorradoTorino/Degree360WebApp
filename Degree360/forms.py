
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
        labels = {
            'answer': '',
        }

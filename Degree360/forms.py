
from django.forms import ModelForm, BaseModelFormSet



from Degree360.models import FeedbackProvider, MultiChoiceAnswer, OpenAnswer

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

class OpenAnswerForm(ModelForm):
    
    class Meta:
        model = OpenAnswer
        fields = ['answer']
        labels = {
            'answer': '',
        }
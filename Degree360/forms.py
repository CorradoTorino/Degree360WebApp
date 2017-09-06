
from django.forms import ModelForm



from Degree360.models import FeedbackProvider

class FeedbackProviderForm(ModelForm):
    class Meta:
        model = FeedbackProvider
        fields = ['name', 'last_name', 'email', 'relation_type']

        
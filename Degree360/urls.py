from django.conf.urls import url

from . import views

app_name = 'Degree360'

urlRegexPatterns = {
    'SurveyIndex' :  r'^$',
    'requestFeedback' : r'^requestFeedback/(?P<pk>[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})/$',    
    'feedbackProvider' : r'^feedbackProvider/(?P<pk>[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})/(?P<email>[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)/$',
}

urlpatterns = [
    # ex: 
    url(urlRegexPatterns['SurveyIndex'], views.SurveyIndexView.as_view(), name='SurveyIndex'),
    
    # ex: requestFeedaback/ed521599-062e-4a19-bb2a-419ebc15e29c/
    url(urlRegexPatterns['requestFeedback'], views.requestFeedback, name='requestFeedback'),

    # ex: feedbackProvider/ed521599-062e-4a19-bb2a-419ebc15e29c/dummyGuy@email.com
    url(urlRegexPatterns['feedbackProvider'], views.feedbackProvider, name='feedbackProvider', ),
]

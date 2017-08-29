from django.conf.urls import url

from . import views

app_name = 'Degree360'

urlRegexPatterns = {
    'workInProgress' :  r'^$',
    'requestFeedaback' : r'^(?P<pk>[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})/requestFeedaback/$',
}

urlpatterns = [
    # ex: 
    url(urlRegexPatterns['workInProgress'], views.workInProgress, name='workInProgress'),
    
    # ex: ed521599-062e-4a19-bb2a-419ebc15e29c/requestFeedaback/
    url(urlRegexPatterns['requestFeedaback'], views.requestFeedaback, name='requestFeedaback'),
]

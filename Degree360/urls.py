from django.conf.urls import url

from . import views

app_name = 'Degree360'

urlRegexPatterns = {
    'workInProgress' :  r'^$',
    'requestFeedaback' : r'^requestFeedaback/(?P<pk>[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})/$',
}

urlpatterns = [
    # ex: 
    url(urlRegexPatterns['workInProgress'], views.workInProgress, name='workInProgress'),
    
    # ex: requestFeedaback/ed521599-062e-4a19-bb2a-419ebc15e29c/
    url(urlRegexPatterns['requestFeedaback'], views.requestFeedaback, name='requestFeedaback'),
]

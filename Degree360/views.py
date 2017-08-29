from django.http import HttpResponse
from Degree360.models import FeedbackProvider

def workInProgress(request):
    return HttpResponse("Generic view for Degree360. Work in progress.")

def requestFeedaback(request, pk):
    feedbackProviders = FeedbackProvider.objects.all()
    pseudoHead = "!!requestFeedaback view.. work in progress!! You're looking at 360 Degree feedback survey %s." % pk
    names = ', '.join([fp.name for fp in feedbackProviders])
    output = pseudoHead + names
    return HttpResponse(output)

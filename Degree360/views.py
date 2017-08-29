from django.http import HttpResponse
from django.shortcuts import render

from Degree360.models import FeedbackProvider

def workInProgress(request):
    return HttpResponse("Generic view for Degree360. Work in progress.")

def requestFeedaback(request, pk):
    feedbackProviders = FeedbackProvider.objects.all()
    context = {
        'pk': pk,
        'feedbackProviders': feedbackProviders
        }
    
    return render(request, 'Degree360/requestFeedback.html', context)

from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.forms import ModelForm
from django.views.generic.edit import FormView
from django.http import HttpResponse, HttpResponseRedirect
from Degree360.forms import FeedbackProviderForm
from django import forms

from Degree360.models import FeedbackProvider, Survey

def workInProgress(request):
    return HttpResponse("Generic view for Degree360. Work in progress.")

def requestFeedback(request, pk):
    feedbackProviders = FeedbackProvider.objects.all()
    context = {
        'pk': pk,
        'feedbackProviders': feedbackProviders
        }
    
    return render(request, 'Degree360/requestFeedback.html', context)

def feedbackProvider(request, pk, email):   
    feedbackProvider = get_object_or_404(FeedbackProvider, survey=pk, email=email)  
    template = 'Degree360/FeedbackProvider.html'
    
    if request.method == "POST":
        form = FeedbackProviderForm()
        
        form = FeedbackProviderForm(request.POST, instance=feedbackProvider)
        if form.is_valid():
            feedbackProvider = form.save(commit=False)
            feedbackProvider.survey = Survey.objects.get(id=pk)
            feedbackProvider.email = email
            feedbackProvider.save()
            return HttpResponse("feedbackProvider Work in progress: saved the feedbackProvider")
    else:
        initial = {
            'name': feedbackProvider.name,
            'last_name': feedbackProvider.last_name,            
            'relation_type': feedbackProvider.relation_type
            }
        form = FeedbackProviderForm(initial)
        
    
    return render(request, template, {'form':form})




from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages 
from django.views.generic import ListView
from django.forms import BaseModelFormSet
from django.forms import ModelForm
from django.forms import modelformset_factory, modelform_factory
from django import forms

from django.core.urlresolvers import reverse

from Degree360.models import FeedbackProvider, Survey, QuestionSection, Question, MultiChoiceAnswer, OpenAnswer

from Degree360.forms import MultiChoiceAnswerForm, FeedbackProviderForm

def workInProgress(request):
    return HttpResponse("Generic view for Degree360. Work in progress.")

def requestFeedback(request, pk):
    feedbackProviders = FeedbackProvider.objects.all()
    context = {
        'pk': pk,
        'feedbackProviders': feedbackProviders
        }
    
    return render(request, 'Degree360/requestFeedback.html', context)

def _createFormSet(request, queryset):
    form = modelformset_factory(MultiChoiceAnswer, form=MultiChoiceAnswerForm, extra=0)    
    return form(request.POST or None, queryset=queryset, )

def _redirectToNextSectionOrCloseFeedback(survey, email, currentSection):
    #redirect to the next question
    sections = QuestionSection.objects.filter(survey = survey).order_by('order')
    currentSectionObject = QuestionSection.objects.get(survey = survey, description = currentSection)
    for availableSection in sections:
        if availableSection.order > currentSectionObject.order:
            return HttpResponseRedirect(reverse('Degree360:questionSectionView', args=(survey, email, availableSection.description,)))
    return HttpResponse("Good all section are replied. now save the survey....")
                    
def questionSectionView(request, pk, email, section):

    feedbackProvider = get_object_or_404(FeedbackProvider, survey=pk, email=email)
    multiChoiceAnswers = MultiChoiceAnswer.objects.filter(feedback_provider = feedbackProvider, question__section__description = section)
    formSet = _createFormSet(request, multiChoiceAnswers)
    
    if request.method == "POST":
        validationErrorFound = False
        if formSet.is_valid():
            for form in formSet:
                if form.is_valid():
                    form.save()
                else:
                    validationErrorFound = True
                    #Todo: add error in the form. Investigate it
                    
            if(validationErrorFound == False):
                return _redirectToNextSectionOrCloseFeedback(pk, email, section)
                                                
    #formSet = form(queryset = multiChoiceAnswers, )
    context = {
        'pk': pk,
        'section': section,
        'formSet': formSet,
        }        
                   
    return render(request, 'Degree360/questionSection.html', context)
    
def _processFeedbackProviderFormAndRedirect(form, pk):
    if form.is_valid():
        feedbackProvider = form.save(commit=False)
        feedbackProvider.survey = Survey.objects.get(id=pk)
        feedbackProvider.save()
        return HttpResponseRedirect(reverse('Degree360:requestFeedback', args=(pk,)))
    
def _renderFeedbackProviderTemplate(request, form, pk):
    template = 'Degree360/FeedbackProvider.html'
    context = {
        'form':form,
         'pk':pk
         }
    
    return render(request, template, context)

def addFeedbackProvider(request, pk):
    if request.method == "POST":
        form = FeedbackProviderForm(request.POST)
        _processFeedbackProviderFormAndRedirect(form, pk)
    else:
        form = FeedbackProviderForm()

    return _renderFeedbackProviderTemplate(request, form, pk)

def editFeedbackProvider(request, pk, email):   
    feedbackProvider = get_object_or_404(FeedbackProvider, survey=pk, email=email)  
        
    if request.method == "POST":      
        form = FeedbackProviderForm(request.POST, instance=feedbackProvider)
        _processFeedbackProviderFormAndRedirect(form, pk)
    else:
        initial = {
            'name': feedbackProvider.name,
            'last_name': feedbackProvider.last_name,
            'email': feedbackProvider.email,
            'relation_type': feedbackProvider.relation_type
            }
        form = FeedbackProviderForm(initial)

    return _renderFeedbackProviderTemplate(request, form, pk)

class SurveyIndexView(ListView):
    template_name = 'Degree360/SurveyIndex.html'
    context_object_name = 'surveys_list'
    
    def get_queryset(self):
        return Survey.objects.all()



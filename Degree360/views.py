from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages 
from django.views.generic import ListView

from django.core.urlresolvers import reverse

from Degree360.forms import FeedbackProviderForm

from Degree360.models import FeedbackProvider, Survey, QuestionSection, Question, MultiChoiceAnswer, OpenAnswer
from _overlapped import NULL

def workInProgress(request):
    return HttpResponse("Generic view for Degree360. Work in progress.")

def requestFeedback(request, pk):
    feedbackProviders = FeedbackProvider.objects.all()
    context = {
        'pk': pk,
        'feedbackProviders': feedbackProviders
        }
    
    return render(request, 'Degree360/requestFeedback.html', context)

def questionSectionView(request, pk, email, section):
    
    questionSection = get_object_or_404(QuestionSection, survey=pk, description=section)
    feedbackProvider = get_object_or_404(FeedbackProvider, survey=pk, email=email)
    
    questions = Question.objects.filter(section=questionSection).order_by('order')
    multiChoiceAnswers = MultiChoiceAnswer.objects.filter(feedback_provider = feedbackProvider)
    
    questionsAndAnswers = []
    
    for question in questions:
        correlatedAnswer = NULL
        for multiChoiceAnswer in multiChoiceAnswers:
            if multiChoiceAnswer.question == question:
                correlatedAnswer = multiChoiceAnswer
        
        if correlatedAnswer == NULL:
            correlatedAnswer = MultiChoiceAnswer.create(feedbackProvider, question)
            
        questionsAndAnswers.append((question.text, correlatedAnswer.answer.__str__()))
        
    context = {
        'pk': pk,
        'section': section,
        'questionsAndAnswers': questionsAndAnswers
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



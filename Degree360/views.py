from django.http import HttpResponse

def workInProgress(request):
    return HttpResponse("Generic view for Degree360. Work in progress.")

def requestFeedaback(request, pk):
    return HttpResponse("!!requestFeedaback view.. work in progress!! You're looking at 360 Degree feedback survey %s." % pk)
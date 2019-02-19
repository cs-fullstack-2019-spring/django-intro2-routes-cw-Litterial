from django.shortcuts import render

# Create your views here.


# App request
from django.http import HttpResponse

def index(request):  #Home page
    return HttpResponse("This is the homepage.")

def happyjoy(request):  #endpoint
    return HttpResponse("Happy Happy Joy Joy Happy Joy Joy Happy Joy Joy Joy")#reponse
def young(request):
    return HttpResponse('I barely remember watching Ren and Stimpy. I was at least 3 or 4 when I was watching it.')
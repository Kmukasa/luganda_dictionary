from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
# Create your views here.

def index(request):
    # return HttpResponse("At index of dictionary")
    return render(request, "home.html", {})

def search(request):
    # add search capabilities
    # response = self.client.get('/api/translations/')
    return HttpResponse("Search Endpoint")

def addWord(request):
    # adding new words to the database
    return HttpResponse("Add Endpoint")

def editTranslation(request):
    #editing
    return HttpResponse("Edit endpoint")
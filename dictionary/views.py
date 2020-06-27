from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
import requests
import json

# Create your views here.

def index(request):
    # return HttpResponse("At index of dictionary")
    return render(request, "home.html", {})

def search(request):
    search = request.GET.get('search')
    opt = request.GET.get('option') 

    if search == '':
        return render(request, "home.html", {})
    else:
        api_response = requests.get('http://127.0.0.1:8000/api/translations/?search='+search, params=request.GET)
        data = api_response.json()
        data[0]['option'] = opt
        print(data[0])
        return render(request, "search.html", data[0])


''' { 
        'option' : 'Luganda - English', 
        'searched_word' : 'sugar',
        'word_form' : 'noun', 
        'translation' : 'ssukaali', 
        'example' : 'Please pass the sugar!'
    } '''

'''{
    'option' : 'Luganda - English',
    'search_word' : 'sugar',
    search_results: [
                        {
                            'luganda_word': 'ssukaali',
                            'english_word': 'sugar',
                            'word_form' : 'noun',
                            'english_example' : 'Leta ssukaali', 
                            'luganda_example' : 'Please pass the sugar!
                        },
                    ]
}'''

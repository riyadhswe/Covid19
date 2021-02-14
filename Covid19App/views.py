from django.shortcuts import render
import  requests

# Create your views here.

def index(request):
    data = True
    result = None
    globalSummary = None
    countries = None;
    while(data):
        try:
            result = requests.get('https://api.covid19api.com/summary')
            json = result.json()
            globalSummary = json['Global']
            countries = json['Countries']

            data = False
        except:
            data = True
    return render(request , 'index.html' ,
                  {'globalSummary' : globalSummary ,
                   'countries' : countries})
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    my_dictionary = {'insert_me':'Aow I am comming from first app help.html'}
    return render(request, 'first_app/help.html', context=my_dictionary)


# Create your views here.

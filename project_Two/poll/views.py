from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(response):
    return HttpResponse("<em>hello from the apps app</em>")


def helpme(response):
    my_dictionary = {'help': ' Help information'}
    return render(response, 'poll/help.html', my_dictionary)

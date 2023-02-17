from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# HTTP REQUEST
def home(req):
    return render(req, 'recipes/home.html', context={
        'name': 'Hícaro Vitor'
    })

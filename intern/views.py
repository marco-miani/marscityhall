from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Intern



def index(request):
    return render(request, 'intern/index.html', {
        'intern': Intern.objects.all()
    })

def view_intern(request, id):
    return HttpResponseRedirect(reverse('index'))
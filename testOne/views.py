from django.shortcuts import render

from testOne.models import TestOne

# Create your views here.
def index(request):
    comps = TestOne.objects.all()
    return render(request, 'testOne/main-page.html', {"comps":comps})

def about(request):
    return render(request, 'testOne/about.html')
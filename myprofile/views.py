from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def top(request):
    context = {
      'name' : 'めめ',
    }
    return render(request, 'myprofile/top.html', context)

def resume(request):
    return render(request, 'myprofile/resume.html')
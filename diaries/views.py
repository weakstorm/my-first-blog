from django.shortcuts import render
from .models import Diary
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def top(request):
  context = {
    'diary_list': Diary.objects.all(),
  }
  return render(request, 'diaries/diary_list.html', context)
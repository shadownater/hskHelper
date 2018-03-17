# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
#Home page
def index(request):
    return  render(request, 'index.html')

def timedQuestionsPage(request):
    return render(request, 'timedQuestions.html')

def speedVocabPage(request):
    return render(request, 'speedVocab.html')

def speedWritingPage(request):
    return render(request, 'speedWriting.html')
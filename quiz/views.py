from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Question
from django.http import JsonResponse
import json


def json(request):
    data = list(Question.objects.values())
    return JsonResponse(data, safe=False)
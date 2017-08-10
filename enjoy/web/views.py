# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Plan
from .forms import PlanForm


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def plans(request):
    if request.method == 'GET':
        plans = Plan.objects.all()
        return render(request, 'plan/index.html', {"plans": plans})
    else:
    	raise Http404()

def plan_post(request):
    if request.method == 'GET':
        form = PlanForm() 
        return render(request, 'plan/post.html', {"form": form})
    elif request.method == 'POST':
        form = PlanForm(request.POST) 
        if form.is_valid():
            form.save()
            return render(request, 'plan/post.html', {"form": form})
        else:
            print(form.errors)
            return render(request, 'plan/post.html', {"form": form})
    else:
        raise Http404()

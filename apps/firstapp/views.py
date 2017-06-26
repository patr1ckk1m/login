# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import User

def index(request):
    return render(request, 'firstapp/index.html')

def success(request):
    return render(request, 'firstapp/success.html')

def register(request):
    res = User.objects.validregister(request.POST)
    if res["status"]:
        request.session['userID'] = res['user'].id
        return redirect('/success')
    else:
        for error in res["errors"]:
            messages.error(request, error)
        return redirect('/')

def login(request):
    res = User.objects.validlogin(request.POST)
    if res['status']:
        request.session['userID'] = res['user'].id
        return redirect('/success')
    else:
        for error in res["errors"]:
            messages.error(request, error)
        return redirect('/')

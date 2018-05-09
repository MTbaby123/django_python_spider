# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response

# Create your views here.
from . import models
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render

def search(request,film_id):
    film = models.Film.objects.filter(pk=film_id)
    return render(request, 'search.html',{'film':film})


def film_result(request,film_id):
    if str(film_id) == "0":
        return render(request, 'search.html')
    film = models.Film.objects.get(pk = film_id)
    return render(request,'film_result.html',{'film':film})














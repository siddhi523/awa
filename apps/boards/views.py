# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .import models

def home_001(request):
    boards = models.Board.objects.all()
    boards_name = list()

    for board in boards:
        boards_name.append(board.name)

    response_html = "<br>".join(boards_name)

    return HttpResponse(response_html)

def home(request):
    boards = models.Board.objects.all()
    return render(request, "home_001.html", {"boards": boards})

#def board_topics(request, pk):
 #   board = models.Board.objects.get(pk=pk)
  #  return render(request, 'topics.html', {'board': board})
    # return HttpResponse("This is a test template")

def board_topics(request,pk):
    board = models.Board.objects.get(pk=pk)
    return render(request, 'topics.html', {'board': board})
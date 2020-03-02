from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    return HttpResponse("eworjf")

def test(request):
    print("这是Dev上的代码与master没有任何关系")
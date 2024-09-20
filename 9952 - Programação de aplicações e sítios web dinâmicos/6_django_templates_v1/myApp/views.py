from lib2to3.fixes.fix_input import context

from django.shortcuts import render

from django.template import loader
from  django.http import HttpResponse


def index(request):
    temp = loader.get_template("index.html")
    return HttpResponse(temp.render())


def info(request):
    contex = {
        'nome': 'Gonçalo',
        'ano': 2024
    }

    temp = loader.get_template("info.html")
    return HttpResponse(temp.render(contex, request))



def nova_view(request):
    contex = {
        'nome': 'Gonçalo 2',
        'ano': 9999,
        'nova_var': 'novo Valor'
    }

    return render(request,"info2.html", contex)
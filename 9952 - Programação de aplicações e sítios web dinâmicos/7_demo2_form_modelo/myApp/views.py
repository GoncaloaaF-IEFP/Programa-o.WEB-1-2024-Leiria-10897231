from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from .models import Aluno
from .forms import  AlunoForm
import django


# Create your views here.

def index(request):

    Aluno.objects.create(name="nome do aluno 2",
                         idade = 11,
                         turma= "IEFP Web 2"
                        )

    return HttpResponse("Hello, world")


def index2(request):
    al = Aluno(name="nome do aluno 2",
                         idade=11,
                         turma="IEFP Web 2"
                         )

    al.save()

    return HttpResponse("Hello, world")



#...?nome=Goncalo&idade=19&turma=IEFP
def index3(request):
    nome = request.GET.get('nome', 'Sem nome')
    idade = request.GET.get('idade', -1)
    turma = request.GET.get('turma', "Sem turma")

    al = Aluno(name=nome, idade=idade, turma=turma)
    al.save()

    return HttpResponse(f"aluno {al.id},  nome: {nome} salvo")


def lista(request):

    #carregar a lista
    lista = Aluno.objects.all().values()

    return render(request,
                  'lista.html',
                  {'lista': lista})


def addAluno(request):
    return render(request, "form1.html")


def addData(request):

    if request.method == "POST":

        print(request.POST)

        form = AlunoForm(request.POST)

        if form.is_valid():

            aluno = Aluno(name=form.cleaned_data['nome'],
                          idade=form.cleaned_data['idade'],
                          turma=form.cleaned_data['turma'])

            aluno.save()

        return HttpResponseRedirect("/lista/")
    else:

        return HttpResponseRedirect("/add/")


def addAluno2(request):

    form = AlunoForm()

    return render(request,
                  "form2.html",
                  {'form': form}
                  )


# .../{id}
def getAluno(request, aluno_id:int):
    try:
        aluno = Aluno.objects.get(id=aluno_id)

        print(aluno)

        return HttpResponse(f"Aluno com o id: {aluno.id}, nome: {aluno.name}")

    except:
        raise Http404 # não e a melhor opt
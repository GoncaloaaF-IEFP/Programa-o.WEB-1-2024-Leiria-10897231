from django.urls import path

from . import views

urlpatterns = [
    path("save1/", views.index, name="index"),
    path("save2/", views.index2, name="save2"),
    path("save3/", views.index3, name="save3"),

    path("lista/", views.lista, name="lista"),

    path("add/", views.addAluno, name="add"),

    path("addData/", views.addData, name="addAluno"),

    path("add2/", views.addAluno2, name="addAluno2"),

    path("aluno/<int:aluno_id>", views.getAluno, name="aluno"),

]


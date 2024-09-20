from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('info/', views.info, name="info"),

    path('info2/', views.nova_view, name="info2"),
]
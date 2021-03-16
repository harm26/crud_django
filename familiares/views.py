from django.shortcuts import render, redirect
from familiares.models import Familiares
from .forms import *
from rest_framework import generics
from .serializer import FamiliaresSerializers

# Create your views here.

class FamiliaresList(generics.ListCreateAPIView):
    queryset = Familiares.objects.all()
    serializer_class = FamiliaresSerializers

class FamiliaresDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Familiares.objects.all()
    serializer_class = FamiliaresSerializers



def inicio(request):
    familiares= Familiares.objects.all()
    title = 'FAMILIARES'
    contexto = {'familiares': familiares, 'title': title}
    return render(request, 'familiares/inicio.html', contexto)

def crear(request):
    form = FormFamiliares()
    if request.method == 'POST':
        form = FormFamiliares(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    contexto = {'form': form}
    return render(request, 'familiares/crear.html', contexto)

def editar(request,id):

    familiar = Familiares.objects.get(id=id)
    if request.method == 'POST':
        form = FormFamiliares(request.POST, instance=familiar)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = FormFamiliares(instance=familiar)
    contexto={'form': form}
    return render(request, 'familiares/editar.html', contexto)

def eliminar(request, id):
    familiar= Familiares.objects.get(id=id)

    if request.method == 'POST':
        familiar.delete()
        return redirect('/')
    contexto={'familiar': familiar}
    return render(request, 'familiares/eliminar.html', contexto)
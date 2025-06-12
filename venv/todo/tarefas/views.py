from django.shortcuts import render
from .models import Tarefa, Usuario, VendaSaida
from datetime import datetime
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import VendaSaidaForm

from .serializers import UsuarioSerializer, TarefaSerializer, VendaSaidaSerializer
from rest_framework import viewsets, permissions

class TarefaViewSet(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    permission_classes = [permissions.AllowAny]

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class VendaSaidaViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite que as vendas sejam visualizadas ou editadas.
    """
    queryset = VendaSaida.objects.all()
    serializer_class = VendaSaidaSerializer

def formlogin(request):

    if request.method == "POST":
        usuario = request.POST['login']
        senha = request.POST['senha']        
        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/tarefas/listartarefas")
    
    return render(request, "login.html")

def logout_view(request):
    logout(request)

    return HttpResponseRedirect("/tarefas/login")

@login_required(login_url="/tarefas/login")
def listarTarefas(request):

    if request.method == "GET" and request.GET.get('busca'):
        tarefas = Tarefa.objects.filter(titulo__icontains=request.GET.get('busca'))
    else:
        tarefas = Tarefa.objects.all()

    return render(request, "listarTarefas.html", {"tarefas" : tarefas})

@login_required(login_url="/tarefas/login")
def listarUsuarios(request):

    usuarios = Usuario.objects.all()

    return render(request, "listarUsuarios.html", {"usuarios": usuarios})

@login_required(login_url="/tarefas/login")
def cadastroAtividade(request):

    if(request.method == "POST"):
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')        
        ano = int(request.POST.get('data').split("-")[0])
        mes = int(request.POST.get('data').split("-")[1])
        dia = int(request.POST.get('data').split("-")[2])
        data = datetime(ano, mes, dia)
        usuario = Usuario.objects.get(id=request.POST.get('usuario'))

        nova_atividade = Tarefa(titulo=titulo, 
                                descricao=descricao, 
                                data=data, 
                                usuario=usuario)
        nova_atividade.save()

        return HttpResponseRedirect('/tarefas/listartarefas')

    usuarios = Usuario.objects.all()

    return render(request, "cadastroAtividade.html", {'usuarios':usuarios})

@login_required(login_url="/tarefas/login")
def cadastroUsuario(request):
    return render(request, "cadastroUsuario.html")

@login_required(login_url="/tarefas/login")
def excluirAtividade(request, id):

    tarefa = Tarefa.objects.get(id=id)
    tarefa.delete()

    return HttpResponseRedirect('/tarefas/listartarefas')

@login_required(login_url="/tarefas/login")
def editarAtividade(request, id):

    if request.method == "POST":
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')        
        ano = int(request.POST.get('data').split("-")[0])
        mes = int(request.POST.get('data').split("-")[1])
        dia = int(request.POST.get('data').split("-")[2])
        data = datetime(ano, mes, dia)
        usuario = Usuario.objects.get(id=request.POST.get('usuario'))

        editar_atividade = Tarefa.objects.get(id=id)
        editar_atividade.titulo = titulo
        editar_atividade.descricao = descricao
        editar_atividade.data = data
        editar_atividade.usuario = usuario
        editar_atividade.save()

        return HttpResponseRedirect('/tarefas/listartarefas')
    else:
        tarefa = Tarefa.objects.get(id=id)
        usuarios = Usuario.objects.all()

    return render(request, "editarAtividade.html",{'tarefa': tarefa, 'usuarios':usuarios})

def registrar_venda(request):
    if request.method == 'POST':
        form = VendaSaidaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('listarVendas')  # Redirecionar para a listagem de vendas (a ser criada)
    else:
        form = VendaSaidaForm()
    return render(request, 'cadastroVenda.html', {'form': form})

def listarVendas(request):
    vendas = VendaSaida.objects.all().order_by('-data_venda')
    return render(request, 'listarVendas.html', {'vendas': vendas})
from django.shortcuts import  render, redirect,HttpResponse
from django.views.generic import TemplateView,View

from .forms import ContatoForm
from .models import Agendamento
from django.views.generic import View


class Home(View):
     def get(self, request):
          form = ContatoForm()
          return render(request, 'index.html', {'form':form})

     def post(self, request):
          form = ContatoForm(request.POST)
          if form.is_valid():
               agendamento = Agendamento(
                    nome = form.cleaned_data['nome'],
                    email=form.cleaned_data['email'],
                    opcoes=form.cleaned_data['opcoes'],
                    horario=form.cleaned_data['horario'],
                    local=form.cleaned_data['local'],
                    data=form.cleaned_data['data'],
                    protocolo=form.cleaned_data['protocolo'],
               )
               agendamento.save()
               form.send_email()
               form = ContatoForm()
          else:
               form = ContatoForm()
          context = {
               'form' : form
          }
          return render(request, 'index.html', context)


def index(request):
     if(request.method) == 'POST':
          form = ContatoForm(request.POST)
          if form.is_valid():
               agendamento = Agendamento(
                    nome = form.cleaned_data['nome'],
                    email=form.cleaned_data['email'],
                    opcoes=form.cleaned_data['opcoes'],
                    horario=form.cleaned_data['horario'],
                    local=form.cleaned_data['local'],
                    data=form.cleaned_data['data'],
                    protocolo=form.cleaned_data['protocolo'],
               )
               agendamento.save()
               form.send_email()
               form = ContatoForm()
     else:
          form = ContatoForm()
     context = {
          'form' : form
     }
     return render(request, 'index.html', context)
          




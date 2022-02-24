from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from .models import Empresa

class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['nome']

    # sobescrevendo o metodo form_valid 
    # para atualizar a empresa do funcionario
    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj
        funcionario.save()
        return HttpResponse('ok')


class EmpresaEdit(UpdateView):
    model = Empresa
    fields = ['nome']
    

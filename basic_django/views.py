from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def view_1(request):
  template = loader.get_template('index.html')
  context = {
    'Var1': "template2",
    'Variable1': 'View 2',
    'Var2': "template3",
    'Variable2': 'View 3',
  }
  return HttpResponse(template.render(context, request))

def view_2(request):
  template = loader.get_template('index.html')
  context = {
    'Var1': "template3",
    'Variable1': 'View 3',
    'Var2': "template1",
    'Variable2': 'View 1',
  }
  return HttpResponse(template.render(context, request))

def view_3(request):
  template = loader.get_template('index.html')
  context = {
    'Var1': "template1",
    'Variable1': 'View 1',
    'Var2': "template2",
    'Variable2': 'View 2',
  }
  return HttpResponse(template.render(context, request))

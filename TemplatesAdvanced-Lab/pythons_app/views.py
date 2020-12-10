# from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from pythons_core.decorators import group_required
from .forms import PythonCreateForm
from .models import Python


# Create your views here.


def index(req):
    pythons = Python.objects.all()
    for python in pythons:
        if python.wishes_set.filter(user_id=req.user.id).exists():
            python.is_wished = True
        else:
            python.is_wished = False
    context = {
        'pythons': pythons,
        'current_page': 'home',
    }
    return render(req, 'index.html', context)


@login_required
@group_required(groups=['Regular User'])
def create(req):
    if req.method == 'GET':
        form = PythonCreateForm()
        context = {
            'form': form,
            'current_page': 'create'
        }
        return render(req, 'create.html', context)
    else:
        data = req.POST
        form = PythonCreateForm(data)
        print(form)
        if form.is_valid():
            python = form.save()
            python.save()
            return redirect('index')

        context = {
            'form': form,
            'current_page': 'create'
        }
        return render(req, 'create.html', context)


# def python_details(request, pk):
#     python = Python.objects.get(pk=pk)
#     context = {
#         'python': python,
#     }
#     return render(request, 'pythons/details.html', context)


# def wish_python(request, pk):
#     python = Python.objects.get(pk=pk)
#     if python.wishes_set.filter(id=request.user.id).exists():
#         python.wishes_set.remove(request.user)
#     else:
#         python.wishes_set.add(request.user)
#     return redirect('index')

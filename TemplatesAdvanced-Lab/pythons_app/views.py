# from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import PythonCreateForm
from .models import Python


# Create your views here.
from .pythons_core.decorators import group_required


def index(req):
    pythons = Python.objects.all()
    context = {
        'pythons': pythons,
        'current_page': 'home'
    }
    return render(req, 'index.html', context)


# @login_required(login_url='login user')
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

import os
import urllib.parse
from os.path import join, isfile

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from resources.forms import PetForm
from resources.models import Pet


def pets(request):
    if request.method == 'GET':
        context = {
            'pets': Pet.objects.all(),
            'form': PetForm()
        }
        return render(request, 'resources/pet/pets.html', context)
    else:
        '''When receiving files, you should have request.FILES!'''
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pets')

        '''
        When returning a failed POST,
        you should return the same form instead of creating a new one,
        because the errors are stored inside the form!
        '''
        context = {
            'pets': Pet.objects.all(),
            'form': form
        }
        return render(request, 'resources/pet/pets.html', context)


def fix_path(path):
    path = urllib.parse.unquote(path)

    return path.replace('/', os.path.sep)


def get_public_file(request, path_to_file):
    full_path = fix_path(join(settings.MEDIA_ROOT, 'public', path_to_file[len('/media/public/'):]))

    if isfile(full_path):
        has_access = True
        if has_access:
            file = open(full_path, 'rb')
            response = HttpResponse(content=file)
            response['Content-Disposition'] = 'attachment'
            return response
    return None


def get_private_file(request, path_to_file):
    full_path = join(settings.MEDIA_ROOT, 'private', path_to_file[len('/media/private/'):])
    if '/' in full_path:
        full_path = fix_path(full_path)

    if isfile(full_path):
        has_access = True
        if has_access:
            file = open(full_path, 'rb')
            response = HttpResponse(content=file)
            response['Content-Disposition'] = 'attachment'
            return response
    return None

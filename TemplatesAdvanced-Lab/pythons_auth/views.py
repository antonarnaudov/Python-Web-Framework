from django.contrib.auth import logout, authenticate, login
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import redirect, render

from pythons_app.models import Wishes, Python
from pythons_auth.forms import RegisterForm, ProfileForm, LoginForm


def get_redirect_url(params):
    redirect_url = params.get('return_url')
    return redirect_url if redirect_url else 'index'


@transaction.atomic
def register_user(request):
    if request.method == 'GET':
        context = {
            'user_form': RegisterForm(),
            'profile_form': ProfileForm(),
        }
        return render(request, 'auth/register.html', context)

    else:
        user_form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        redirect_url = get_redirect_url(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)

            user.groups.add(1)
            profile.user = user
            profile.save()

            login(request, user)
            return redirect(redirect_url)

        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }
        return render(request, 'auth/register.html', context)


def login_user(request):
    if request.method == 'GET':
        context = {
            'login_form': LoginForm()
        }
        return render(request, 'auth/login.html', context)
    else:
        login_form = LoginForm(request.POST)
        redirect_url = get_redirect_url(request.POST)

        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect(redirect_url)
        context = {
            'login_form': login_form,
        }
        return render(request, 'auth/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('index')


@login_required
def wish_python(request, pk):
    redirect_url = get_redirect_url(request.POST)
    wishes = Wishes.objects.filter(user_id=request.user.id, python_id=pk).first()
    if wishes:
        wishes.delete()
    else:
        python = Python.objects.get(pk=pk)
        wish = Wishes(user=request.user)
        wish.python = python
        wish.save()
    return redirect(redirect_url)


def view_wishlist(request):
    context = {
        'wishlist': request.user.wishes_set.all(),
    }
    return render(request, 'wishlist.html', context)
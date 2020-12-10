from django.http import HttpResponse


def group_required(groups=None):
    if groups is None:
        groups = []

    groups_set = set(groups)

    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if request.user.is_superuser:
                return view_func(request, *args, **kwargs)

            #  request.user.groups.only('name')
            # --> returns only the id and the requested object/s, ypu can ask for many!

            user_groups = set([group.name for group in request.user.groups.all()])

            if user_groups.intersection(groups_set):
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('<h1>You are not authorized!</h1>')

        return wrapper

    return decorator

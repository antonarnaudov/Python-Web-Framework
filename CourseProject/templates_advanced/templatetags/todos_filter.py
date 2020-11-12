from django import template

register = template.Library()


# can change state to True
@register.filter
def todos_filter(todos, state=False):
    return [todo for todo in todos if todo.is_done is state]

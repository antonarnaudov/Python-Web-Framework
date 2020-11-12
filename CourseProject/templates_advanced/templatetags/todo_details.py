from django import template

from templates_advanced.models import Todo

register = template.Library()

'''Simple tag is used to return some text'''


# @register.simple_tag()
# def todo_details(todo):
#     return f'<h1>{todo.text}</h1>'

@register.inclusion_tag('templates_advanced/tags/todo_item.html')
def todo_details(todo):
    return {
        'todo': todo,
        'todos_count': Todo.objects.count(),
    }

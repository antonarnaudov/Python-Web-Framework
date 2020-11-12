from django import template

register = template.Library()

'''AUTOMATED BOOTSTRAP CLASS ADDERS FOR FORMS'''


@register.inclusion_tag('templates_advanced/tags/bootstrap_form.html')
def bootstrap_form(form, action, method):
    # Making sure we are not overriding a class

    for (_, field) in form.fields.items():
        if not field.widget.attrs['class']:
            field.widget.attrs['class'] = ''
        else:
            field.widget.attrs['class'] += ' form-control'

    return {
        'form': form,
        'action': action,
        'method': method,
    }

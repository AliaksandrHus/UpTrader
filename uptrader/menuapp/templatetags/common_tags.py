from django import template
from ..models import Menu

register = template.Library()

@register.inclusion_tag('templatetags/menu.html', takes_context=True)
def show_top_menu(context):

    menu = Menu.objects.all()

    return {"menu": menu}

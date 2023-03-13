from django import template

from store.models import Category

register = template.Library()

@register.inclusion_tag('template_tags/draw_categorys.html', name='draw_categorys')
def draw_categorys():
    return {
            'categorys': Category.objects.all()[:5]
        }

from django import template

register = template.Library()


@register.filter(name='get_filter_values')
def get_filter_values(value):
    return value.getlist('filters')


@register.filter(name='get_filter_link')
def get_filter_values(request, tag):
    new_request = request.GET.copy()
    if tag.value in request.GET.getlist('filters'):
        filters = new_request.getlist('filters')
        filters.remove(tag.value)
        new_request.setlist('filters', filters)
    else:
        new_request.appendlist('filters', tag.value)
        new_request.setlist('page', '1')
    return new_request.urlencode()


@register.simple_tag(takes_context=True)
def generate_page_url(context, **kwargs):
    query = context['request'].GET.copy()
    for k, v in kwargs.items():
        query[k] = v
    for k in [k for k, v in query.items() if not v]:
        del query[k]
    return query.urlencode()

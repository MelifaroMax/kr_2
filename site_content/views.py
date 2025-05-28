from django.shortcuts import render, get_object_or_404
from .models import PageContent

from django.shortcuts import render
from .models import PageContent

def pages_home(request):
    sort_by = request.GET.get('sort', 'title')
    direction = request.GET.get('direction', 'asc')
    filter_title = request.GET.get('title', '')

    pages = PageContent.objects.all()

    if filter_title:
        pages = pages.filter(title__icontains=filter_title)

    if sort_by not in ['title', 'slug', 'id']:
        sort_by = 'title'

    if direction == 'desc':
        sort_by = '-' + sort_by

    pages = pages.order_by(sort_by)

    context = {
        'pages': pages,
        'current_sort': request.GET.get('sort', 'title'),
        'current_direction': direction,
        'filter_title': filter_title,
    }
    return render(request, 'site_content/pages_home.html', context)


def page_detail(request, slug):
    page = get_object_or_404(PageContent, slug=slug)
    return render(request, 'site_content/page_detail.html', {'page': page})

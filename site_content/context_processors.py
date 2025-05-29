from .models import PageContent

def pages_menu(request):
    pages = PageContent.objects.all()
    return {'pages_menu': pages}


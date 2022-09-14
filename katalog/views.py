from django.shortcuts import render
from katalog.models import CatalogItem

def show_catalog(request):
    data_catalog = CatalogItem.objects.all()
    context = {
        'list_catalog': data_catalog,
        'name': 'Elsa Giana Abigail Sitompul',
        'npm': '2106707252'
    }
    return render(request, "katalog.html", context)
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from mywatchlist.models import WatchList

# Create your views here.
def show_mywatchlist(request):
    data_watchlist = WatchList.objects.all()
    context = {
        'list_watchlist': data_watchlist,
        'name': 'Elsa Giana Abigail Sitompul',
        'npm': '2106707252',
    }
    return render(request, "mywatchlist.html", context)

def show_mywatchlist_xml(request):
    data_watchlist = WatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data_watchlist), content_type="application/xml")

def show_mywatchlist_json(request):
    data_watchlist = WatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data_watchlist), content_type="application/json")    
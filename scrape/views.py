from django.shortcuts import HttpResponse
import django_rq
# Create your views here.
from .models import *
from .scraping import Scrape

def scrapingView(request):
    queue = django_rq.get_queue('default',is_async=True,default_timeout=30000)
    queue.enqueue(Scrape)

    return HttpResponse("Scraping Articles")


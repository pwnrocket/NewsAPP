from django.urls import path,include

from .views import scrapingView


urlpatterns = [
    path('',scrapingView,name='scrapingFunction'),

]
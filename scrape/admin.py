from django.contrib import admin

# Register your models here.
from .models import *

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','title','author','pub_date','url')



admin.site.register(Article,ArticleAdmin)
admin.site.register(Author)

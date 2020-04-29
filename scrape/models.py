from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.TextField()
    body = models.TextField()
    author = models.ForeignKey(Author,related_name="ArticleAuthor",on_delete=models.PROTECT)
    url = models.URLField(max_length=1000)
    pub_date = models.CharField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ArticleStatus(models.Model):
    article = models.ForeignKey(Article,related_name="TheArticle",on_delete=models.PROTECT)
    status =  models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ScrapeHistory(models.Model):
    article = models.ForeignKey(Article,related_name="ScrapedArticle",on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
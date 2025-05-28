from django.db import models

# Create your models here.

class PageContent(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)  # для url
    content = models.TextField()

    def __str__(self):
        return self.title

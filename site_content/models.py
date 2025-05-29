from django.db import models

class PageContent(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to='page_images/', blank=True, null=True)  # новое поле для картинки

    def __str__(self):
        return self.title


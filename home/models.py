from django.db import models

# Create your models here.

# Roadmap

class Roadmap(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=50, default="🌐")  # optional (emoji/icon name)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
    
# News 

class News(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    published_date = models.DateField(auto_now_add=True)
    source = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title


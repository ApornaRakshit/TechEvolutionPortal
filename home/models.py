from django.db import models

# Create your models here.

# Roadmap

class Roadmap(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=50, default="🌐")  # Optional
    link = models.URLField(blank=True, null=True)

    # New fields for your dynamic UI
    duration_weeks = models.IntegerField(default=4)  # Example: 4 weeks
    level = models.CharField(max_length=50, choices=[
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
        ('All Levels', 'All Levels'),
    ], default='Beginner')
    tutorial_count = models.IntegerField(default=0)
    learners_count = models.IntegerField(default=0)
    progress = models.IntegerField(default=0)  # % Progress
    image = models.ImageField(upload_to='roadmaps/', blank=True, null=True)

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


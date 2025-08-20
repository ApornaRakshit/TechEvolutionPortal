from django.shortcuts import render
from .models import Roadmap, News

# Homepage
def index(request):
    roadmaps = Roadmap.objects.all().order_by('-id')[:3]   # show latest 3
    news_articles = News.objects.all().order_by('-published_date')[:3]  # show latest 3
    return render(request, "home/index.html", {
        "roadmaps": roadmaps,
        "news_articles": news_articles
    })

# Full home (if you want a different template than index)
def home(request):
    roadmaps = Roadmap.objects.all()
    return render(request, "home/home.html", {"roadmaps": roadmaps})

# Career Roadmap page
def roadmap(request):
    roadmaps = Roadmap.objects.all().order_by('-id')  # show all
    return render(request, "home/roadmap.html", {"roadmaps": roadmaps})

# Tutorials page
def tutorials(request):
    return render(request, "home/tutorials.html")

# Community page
def community(request):
    return render(request, "home/community.html")

# News page
def news(request):
    articles = News.objects.all().order_by('-published_date')
    return render(request, "home/news.html", {"articles": articles})

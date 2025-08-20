from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('roadmap/', views.roadmap, name="roadmap"),
    path('tutorials/', views.tutorials, name="tutorials"),
    path('community/', views.community, name="community"),
    path('news/', views.news, name="news"),
]

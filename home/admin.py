from django.contrib import admin
from .models import Roadmap, News

# Register your models here.
@admin.register(Roadmap)
class RoadmapAdmin(admin.ModelAdmin):
    list_display = ('title', 'level', 'tutorial_count', 'learners_count', 'progress')
    search_fields = ('title', 'description')
    list_filter = ('level',)
admin.site.register(News)
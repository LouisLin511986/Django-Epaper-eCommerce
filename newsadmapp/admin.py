from django.contrib import admin
from .models import NewsUnit

class NewsAdmin(admin.ModelAdmin):
    list_display = ('catego', 'nickname', 'title','pubtime','enabled','press')
    list_filter = ("catego",)
    search_fields = ("nickname", "title", "press",)
 
admin.site.register(NewsUnit, NewsAdmin)

from django.contrib import admin
from news.models import News, Comments


class NewsInline(admin.StackedInline):
    model = Comments
    extra = 1


class NewsAdmin(admin.ModelAdmin):
    inlines = [NewsInline]
    list_filter = ['news_date']


admin.site.register(News,NewsAdmin)

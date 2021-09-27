from django.contrib import admin

# Register your models here.
# what the admin interface for this app is going to look like

from .models import Article, Author, Region

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on')
    search_fields = ['title', 'content']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Author)
admin.site.register(Region)
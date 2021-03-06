from django.contrib import admin
from blog.models import *
from blog.models import Comment
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title','slug','author','body','publish','created','updated','status']
    prepopulated_fields = {'slug':('title',)}
    list_filter=('status','author','created','publish')
    search_fields = ('title','body')
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status','publish']


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','email','post','body','created','updated','active',)
    list_filter = ('active','created','updated')
    search_fields = ('name','email','body')

class Media:
    css = {
            'all': ('css/blog1.css',)
        }



admin.site.register(Comment,CommentAdmin)
admin.site.register(Post,PostAdmin)

from django.contrib import admin
from .models import Post,Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'post_id', 'game', 'updated_on', 'datetime')
    search_fields = ['title']
    list_filter = ('game',)
    prepopulated_fields = {'post_id': ('title',)}
    summernote_fields = ('description',)

# Register your models here.
admin.site.register(Comment)

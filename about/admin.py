from django.contrib import admin
from .models import AdminStory
from django_summernote.admin import SummernoteModelAdmin


@admin.register(AdminStory)
class AboutAdmin(SummernoteModelAdmin):

    summernote_fields = ('stories',)
# Register your models here.

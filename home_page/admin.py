from django.contrib import admin
from .models import HomePage
from django_summernote.admin import SummernoteModelAdmin


@admin.register(HomePage)
class HomePageAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)

# Register your models here.

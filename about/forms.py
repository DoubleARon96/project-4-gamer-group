from .models import AdminStory
from django import forms


class aboutForm (forms.ModelForm):
    class Meta:
        model = AdminStory
        fields = ('title',
                  'stories')

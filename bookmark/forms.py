from django.forms import ModelForm
from .models import Bookmark, Browser


class BookmarkForm(ModelForm):
    class Meta:
        model = Bookmark
        fields = '__all__'


class BrowserForm(ModelForm):
    class Meta:
        model = Browser
        fields = '__all__'

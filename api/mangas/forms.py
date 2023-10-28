from django import forms
from .models import Manga

class MangaForm(forms.ModelForm):
    class Meta:
        model = Manga
        fields = ['id','title', 'author', 'description', 'cover_image', 'manga_file']

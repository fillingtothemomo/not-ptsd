from django import forms
from .models import Chapter, Manga

class MangaForm(forms.ModelForm):
    class Meta:
        model = Manga
        fields = ['title', 'author', 'description', 'cover_image']
class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['manga', 'chapter_number', 'chapter_file']
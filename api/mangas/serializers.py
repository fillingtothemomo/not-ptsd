from mangas.models import Chapter, Manga
from rest_framework import serializers


class MangaSerializer(serializers.ModelSerializer):
   class Meta:
     model=Manga
     fields='__all__'
class ChapterSerializer(serializers.ModelSerializer):
   class Meta:
      model=Chapter
      fields='__all__'
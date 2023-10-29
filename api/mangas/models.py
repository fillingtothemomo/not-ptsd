from django.db import models

def chapter_upload_path(instance,_):
    return f'manga_files/{instance.manga.id}/chapters/{instance.chapter_number}.pdf'

class Manga(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField(null=True)

class Chapter(models.Model):
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE, related_name='chapters')
    chapter_number = models.PositiveIntegerField()
    chapter_file = models.FileField(upload_to=chapter_upload_path)
    base64_images = models.TextField(blank=True, null=True)

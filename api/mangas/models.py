from django.db import models
def manga_pdf_upload_path(instance):
   return f'manga_files/{instance.id}.pdf'

class Manga(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField(null=True)
    cover_image = models.ImageField(upload_to='manga_covers/', null=True, blank=True)
    manga_file = models.FileField(upload_to=manga_pdf_upload_path, null=True)
    base64_images = models.TextField(blank=True, null=True)


# class Chapter(models.Model):
#     manga_file = models.FileField(upload_to=manga_pdf_upload_path, null=True)
#     manga=models.ForeignKey('Manga',on_delete='CASCADE')
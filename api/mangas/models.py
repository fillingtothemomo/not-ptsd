from django.db import models
def manga_pdf_upload_path(instance,filename):
   return f'manga_files/{instance.id}_{filename}'
    
class Manga(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField(null=True)
    cover_image = models.ImageField(upload_to='manga_covers/', null=True)
    manga_file = models.FileField(upload_to=manga_pdf_upload_path, null=True)
    base64=models.TextField(null=True)
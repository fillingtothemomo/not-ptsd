from django.urls import path
from .views import *

urlpatterns = [
    path('add_new_manga/', add_new_manga, name='add-new-manga'),
    path('add_new_chapter/<int:manga_id>/', add_new_chapter, name='add_new_chapter'),

    path('convert_manga/<str:id>', convert_manga_pdf, name='convert-manga-chapter'),
    path('send_image/<str:id>/', send_image, name='send-image'),
    path('convert_images_to_base64/<str:id>', convert_images_to_base64, name='convert-images-to-base64'),

]

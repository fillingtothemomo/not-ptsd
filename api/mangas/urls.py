from django.urls import path
from .views import *

urlpatterns = [
    path('add_new_manga/', add_new_manga, name='add-new-manga'),
    path('convert_manga/<int:manga_id>/',convert_manga_pdf , name='convert_manga_pdf'),
    path('send_image/<int:manga_id>/',send_image , name='send_image'),
    path('convert_image/<int:manga_id>/',convert_images_to_base64 , name='convert_images_to_base64'),

]

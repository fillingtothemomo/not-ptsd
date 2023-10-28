import os
from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage 
from django.shortcuts import render, redirect
from .forms import MangaForm  # Import the MangaForm you created
from pdf2image import convert_from_path
from .models import Manga
from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_code_pb2
# Your PAT (Personal Access Token) can be found in the portal under Authentification
PAT = '4dc15add6e234d3595ec984436e7fed2'
# Specify the correct user_id/app_id pairings
# Since you're making inferences outside your app's scope
USER_ID = 'rockingpenny4'
APP_ID = 'Manga-detection'
# Change these to whatever model and image input you want to use
MODEL_ID = 'nsfw-recognition'
MODEL_VERSION_ID = 'aa47919c9a8d4d94bfa283121281bcc4'

def add_new_manga(request):
    if request.method == 'POST':
        form = MangaForm(request.POST, request.FILES)
        if form.is_valid():
            manga = form.save(commit=False) # Save the manga object first
            manga.save()
            Manga.objects.filter(pk=manga.pk).update(manga_filename=f'manga_files/{manga.id}.pdf')
            form.save_m2m()
           
    else:
        form = MangaForm()

    return render(request, 'add_new_manga.html', {'form': form})

def convert_manga_pdf(request, manga_id):
    try:
        manga = Manga.objects.get(pk=manga_id)
        pdf_file_path =f'media/manga_files/{manga_id}.pdf'
        output_folder = f'media/manga_images/{manga_id}'  # Create a unique folder for each manga

        os.makedirs(output_folder, exist_ok=True)
        print("hello")
        images = convert_from_path(pdf_file_path)
        print("hello1")
        for page_number, img in enumerate(images, start=1):
            image_filename = f'page_{page_number}.jpg'
            print(image_filename)
            image_path = os.path.join(output_folder, image_filename)
            img.save(image_path, 'JPEG')
        Result = "Conversion success"
    except Manga.DoesNotExist:
        Result = "Manga not found"
    except Exception as e:
        Result = f"Conversion failed: {str(e)}"

    return render(request, 'convert_result.html', {'Result': Result})


def send_image(request,manga_id):
    try:
        manga = Manga.objects.get(pk=manga_id)

        folder_dir = f'media/manga_images/{manga_id}/'
        image_files = [os.path.join(folder_dir, file) for file in os.listdir(folder_dir) if file.lower().endswith('.jpg')]

        image_results = []  

        channel = ClarifaiChannel.get_grpc_channel()
        stub = service_pb2_grpc.V2Stub(channel)
        metadata = (('authorization', 'Key ' + PAT),)
        userDataObject = resources_pb2.UserAppIDSet(user_id=USER_ID, app_id=APP_ID)

        for image_file_location in image_files:
            with open(image_file_location, "rb") as f:
                file_bytes = f.read()

            post_model_outputs_response = stub.PostModelOutputs(
                service_pb2.PostModelOutputsRequest(
                    user_app_id=userDataObject,
                    model_id=MODEL_ID,
                    version_id=MODEL_VERSION_ID,
                    inputs=[
                        resources_pb2.Input(
                            data=resources_pb2.Data(
                                image=resources_pb2.Image(
                                    base64=file_bytes
                                )
                            )
                        )
                        ]
                    
                ),
                metadata=metadata
            )

            if post_model_outputs_response.status.code == status_code_pb2.SUCCESS:
                output = post_model_outputs_response.outputs[0]
                predicted_concepts = [(concept.name, concept.value) for concept in output.data.concepts]
                image_results.append({'image_file': image_file_location, 'predicted_concepts': predicted_concepts})
            else:
                image_results.append({'image_file': image_file_location, 'error': f'Clarifai request failed: {post_model_outputs_response.status.description}'})
        
        return JsonResponse({'analysis_results': image_results})

    except Exception as e:
        return JsonResponse({'error': f'Clarifai request failed: {str(e)}'})

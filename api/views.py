# api/views.py
import requests
from io import BytesIO
from django.http import FileResponse, HttpResponse

def download_image(request):
    base_url = 'https://simpleminecraft.ru'
    image_path = '/uploads/posts/2025-03/1742571521_vesennij-vajp-1.png'
    full_url = base_url + image_path

    try:
        response = requests.get(full_url)
        if response.status_code != 200:
            return HttpResponse(f'Ошибка при загрузке: {response.status_code}', status=500)

        image_bytes = BytesIO(response.content)

        return FileResponse(
            image_bytes,
            as_attachment=True,
            filename='vesennij-vajp.png',
            content_type='image/png'
        )
    except Exception as e:
        return HttpResponse(f'Ошибка сервера: {str(e)}', status=500)


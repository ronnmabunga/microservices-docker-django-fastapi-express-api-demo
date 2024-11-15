from django.urls import path, re_path
from django.http import JsonResponse
import requests


def proxy_to_express(request, path):
    target_url = f"http://express:3001/{path}"
    try:
        response = requests.get(target_url)
        return JsonResponse(response.json(), status=response.status_code)
    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": str(e)}, status=500)


def proxy_to_fastapi(request, path):
    target_url = f"http://fastapi:8001/{path}"
    try:
        response = requests.get(target_url)
        return JsonResponse(response.json(), status=response.status_code)
    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": str(e)}, status=500)


urlpatterns = [
    re_path(r"^user-service/(.*)$", proxy_to_express),
    re_path(r"^tasks-service/(.*)$", proxy_to_fastapi),
]

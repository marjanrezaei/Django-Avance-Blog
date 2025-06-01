from django.http import HttpResponse, JsonResponse
import requests
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from .tasks import sendEmail 
import os


def send_email(request):
    """
    A simple view to simulate sending an email.
    """
    sendEmail.delay()  # Call the Celery task to send the email asynchronously
    
    # Return a simple response
    return HttpResponse("Email sent successfully!")


@cache_page(60 * 15)  # Cache this view for 15 minutes
def test(request):
    response = requests.get("https://e36589a2-9f85-4ac0-8dcf-f7b98135d9e9.mock.pstmn.io/test/delay/5")
    return JsonResponse(response.json())


@cache_page(60 * 20)  # Cache for 20 minutes
def weather(request):
    api_key = "8f160f8d25de806ef110dbabe5cb8f50"
    if not api_key:
        return JsonResponse({"error": "API key not set"}, status=500)
    city = "London"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=8f160f8d25de806ef110dbabe5cb8f50"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


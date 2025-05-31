from django.http import HttpResponse, JsonResponse
import requests
from django.core.cache import cache
from .tasks import sendEmail 

def send_email(request):
    """
    A simple view to simulate sending an email.
    """
    sendEmail.delay()  # Call the Celery task to send the email asynchronously
    
    # Return a simple response
    return HttpResponse("Email sent successfully!")

def test(request):
    if cache.get("test_delay_api") is None:
        response = requests.get("https://e36589a2-9f85-4ac0-8dcf-f7b98135d9e9.mock.pstmn.io/test/delay/5")
        cache.set("test_delay_api",response.json(), 60)  # Cache the response for 60 seconds
    return JsonResponse(cache.get("test_delay_api"))

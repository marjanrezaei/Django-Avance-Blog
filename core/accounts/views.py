from django.http import HttpResponse

from .tasks import sendEmail 

def send_email(request):
    """
    A simple view to simulate sending an email.
    """
    sendEmail.delay()  # Call the Celery task to send the email asynchronously
    
    # Return a simple response
    return HttpResponse("Email sent successfully!")

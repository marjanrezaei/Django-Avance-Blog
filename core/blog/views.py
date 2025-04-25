from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from .models import Post

# Create your views here.
# function based view for template 
"""
def indexView(request):
    '''
    a function based view to show index page
    '''
    name = "yashar"
    context = {"name":name}
    return render(request, 'index.html',context)
"""

class IndexView(TemplateView):
    '''
    a class based view to show index page
    '''
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "marjan"
        context["posts"] = Post.objects.all()
        return context
 
    
""" FBV for redirecting to google

from django.shortcuts import redirect
def redirectGoogle(request):
    return redirect("https://www.google.com")
"""

class RedirectToGoogle(RedirectView):
    '''
    a class based view to redirect to google
    '''
    url = "https://www.google.com"
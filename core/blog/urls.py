from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

app_name = "blog"

urlpatterns = [
    path('fbv-index', views.indexView, name='fbv-test'),
    # path('cbv-index', TemplateView.as_view(template_name = "index.html", extra_context = {"name":"marjan"})),
    path('cbv-index',views.IndexView.as_view(), name = 'cbv-index'),
    path('go-to-index', RedirectView.as_view(pattern_name="blog:cbv-index"), name='redirect-to-index')
]
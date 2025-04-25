from django.urls import path
from . import views
from django.views.generic import TemplateView, RedirectView


app_name = "blog"

urlpatterns = [
    # path('fbv-index', views.indexView, name='fbv-test'),
    # path('cbv-index', TemplateView.as_view(template_name = "index.html", extra_context = {"name":"marjan"})),
    path('cbv-index',views.IndexView.as_view(), name = 'cbv-index'),
    # path('go-to-index', RedirectView.as_view(pattern_name="blog:cbv-index"), name='redirect-to-index')
    path('go-to-google', views.RedirectToGoogle.as_view(), name='redirect-to-google'),
    path('post/', views.PostListView.as_view(), name="post-list"),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name="post-detail"),

]
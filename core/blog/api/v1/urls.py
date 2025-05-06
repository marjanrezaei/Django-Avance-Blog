from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter, SimpleRouter

app_name = "api-v1"

router = SimpleRouter()
router.register('post', views.PostModelViewSet, basename='post')
router.register('category', views.CategoryModelViewSet, basename='category')
urlpatterns = router.urls


# urlpatterns = [
#     # path('post/', views.postList, name="post-list"),
#     #  path('post/<int:id>/', views.postDetail, name="post-detail"),
#     # path('post/', views.PostList.as_view(), name="post-list"),
#     # path('post/<int:pk>/', views.PostDetail.as_view(), name="post-detail"),
#     path('post/', views.PostViewset.as_view({'get': 'list', 'post': 'create'}), name="post-list"),
#     path('post/<int:pk>/', views.PostViewset.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name="post-detail"),


# ] 
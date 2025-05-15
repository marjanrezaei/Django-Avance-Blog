
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from .serializers import PostSerializer, CategorySerializer
from ...models import Post, Category
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .paginations import DefaultPagination
from .filters import PostFilter

'''
from rest_framework.decorators import api_view, permission_classes
 @api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def postList(request):
    if request.method == 'GET':
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def postDetail(request, id):
    post = get_object_or_404(Post, pk=id, status=True)
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        post.delete()
        return Response({'detail':'item removed successfully'}, status=204)
        
'''
        
    
'''
class PostList(APIView):
    """getting a list of posts and creating new posts"""
    permission_classes = [IsAuthenticated] 
    serializer_class = PostSerializer # show html form for create new post
    def get(self, request):
        """Retrieving a list of posts """
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        """creating a post with provided data"""
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
'''
    
# class PostList(ListCreateAPIView):
#     """getting a list of posts and creating new posts"""
#     permission_classes = [IsAuthenticated] 
#     serializer_class = PostSerializer # show html form for create new post
#     queryset = Post.objects.filter(status=True)

'''
class PostDetail(APIView):
    """ Getting detail of the post and edit plus removing it. """
    permission_classes = [IsAuthenticated] 
    serializer_class = PostSerializer
    
    def get(self,request, id):
        """ Retrieving the post data """
        post = get_object_or_404(Post, pk=id, status=True)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    def put(self, request, id):
        """ Editing the post data """
        post = get_object_or_404(Post, pk=id, status=True)
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, id):
        """ deleting the post object """
        post = get_object_or_404(Post, pk=id, status=True)
        post.delete()
        return Response({'detail':'item removed successfully'}, status=204)
'''


# class PostDetail(RetrieveUpdateDestroyAPIView):
#     """ Getting detail of the post and edit plus removing it. """
#     permission_classes = [IsAuthenticated] 
#     serializer_class = PostSerializer
#     queryset = Post.objects.filter(status=True)
    

# Example for viewsets in CBV

class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly] 
    serializer_class = PostSerializer 
    queryset = Post.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['title', 'content']
    ordering_fields = ['published_at']
    pagination_class = DefaultPagination
    filterset_class = PostFilter
    
   
   
class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly] 
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    
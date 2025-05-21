from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    RedirectView,
    ListView,
    DetailView,
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post
from .form import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


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
    """
    a class based view to show index page
    """

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
    """
    a class based view to redirect to google
    """

    url = "https://www.google.com"


class PostListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = "blog.view_post"
    model = Post
    # queryset = Post.objects.all()
    context_object_name = "posts"
    paginate_by = 2
    ordering = "-id"

    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)
    #     return posts


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post


"""class PostCreateView(FormView):
    template_name = 'contact.html'
    form_class = PostForm
    success_url = '/blog/post/'
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)"""


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # fields = ['author', 'title', 'content', 'status', 'category', 'published_at']
    form_class = PostForm
    success_url = "/blog/post/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostEditView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    success_url = "/blog/post/"


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = "/blog/post/"

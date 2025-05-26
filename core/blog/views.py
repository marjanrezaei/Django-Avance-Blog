from django.views.generic import (
    TemplateView,
    RedirectView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)
from .models import Post
from .forms import PostForm


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


class PostListApiView(TemplateView):
    template_name = "blog/post_list_api.html"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
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

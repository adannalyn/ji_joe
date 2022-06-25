from audioop import reverse
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from .models import Post

class PostListView(ListView):
    model: Post
    template_name = 'home.html'
    success_url = reverse_lazy("blog:post")
    def get_queryset(self):
        """Return Post """
        return Post.objects.order_by('id')
    
    
class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:post")
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog.html'
    success_url = reverse_lazy("blog:post")
    
class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:post")
    
class PostDeleteView(UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:post")
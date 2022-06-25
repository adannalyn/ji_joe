from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from .models import Post

class PostListView(ListView):
    model: Post
    template_name = 'home.html'
    def get_queryset(self):
        """Return Post """
        return Post.objects.order_by('title')[:5]
    
    
class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    template_name = 'home.html'
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog.html'
    
class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    template_name = 'home.html'
    
class PostDeleteView(UpdateView):
    model = Post
    fields = "__all__"
    template_name = 'home.html'
#Django
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView

#Forms
#from posts.forms import PostForm

#Models
from posts.models import Post
# Create your views here.

class CreatePostView(LoginRequiredMixin, CreateView):
    """Create a new post"""

    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['user'] =  self.request.user
        return context


class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all published posts"""

    template_name = 'posts/feed.html '
    model = Post
    ordering = ('-created',)
    paginate_by = 10
    context_object_name = 'posts'
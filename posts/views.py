#Django
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView


from posts.forms import PostForm
from posts.models import Post

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

    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 50
    context_object_name = 'posts'


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('posts:feed')

    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user = owner)


class PostDetailView(LoginRequiredMixin, DetailView):
    template_name = 'posts/detail.html'
    model = Post
    context_object_name = 'post'
    
    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user = owner)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class PostEditView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'body']
    context_object_name = 'post'
    template_name = 'posts/edit.html'
    success_url = reverse_lazy('posts:feed')
from django.views.generic import ListView
from .models import Post


class PostList(ListView):
    model = Post
    ordering = 'name'
    template_name = 'news.html'
    context_object_name = 'news'


# from typing import Any
from django.utils import timezone
from django.db.models.query import QuerySet
from django.urls import reverse
from blog.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, UpdateView, CreateView,
                                  DetailView, DeleteView)
# Create your views here.

class HomeView(ListView):
    model = Post
    context_object_name = 'posts'

    # def get_queryset(self):
    #     return Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin,CreateView):
    # login_url = '/login/'
    # redirect_field_name = 'blog/post_list.html'
    model = Post 
    fields = ['title', 'content', 'image'] 

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
     


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post 
    fields = ['title', 'content', 'image'] 

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    

    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post 

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_success_url(self):
        return reverse('blog_home_page')
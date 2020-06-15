from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
def index(request):
    context = {
    'posts': Post.objects.all()
    }
    return render(request, 'frontpage/feed.html', context)

class PostListView(ListView):
    model = Post
    template_name = "frontpage/feed.html"
    context_object_name = 'posts'
    ordering = ['-posted']

class PostDetailView(DetailView):
    model = Post
    template_name = "frontpage/post-detail.html"

class PostCreateView(LoginRequiredMixin ,CreateView):
    model = Post
    fields = ['title','desc','img']
    template_name = "frontpage/post_form.html"


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin , UpdateView, UserPassesTestMixin):
    model = Post
    fields = ['title','desc','img']
    template_name = "frontpage/post_form.html"


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "frontpage/post_confirm_delete.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


    def get_success_url(self):
        return reverse('home')

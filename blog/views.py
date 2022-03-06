from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy


# Create your views here.
class BlogView(ListView):
	model = Post
	template_name = 'blog/blog.html'
	ordering = ['-id']


class ArticleDetail(DetailView):
	model = Post
	template_name = 'blog/article_details.html'


class AddBlogView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'blog/add_blog.html'


class UpdateBlogView(UpdateView):
	model = Post
	form_class = EditForm
	template_name = 'blog/edit_blog.html'


class DeleteBlogView(DeleteView):
	model = Post
	template_name = 'blog/delete_blog.html'
	success_url = reverse_lazy('blog')

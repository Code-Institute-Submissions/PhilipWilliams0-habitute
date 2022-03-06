from django.shortcuts import render
from django.views.generic import (
	ListView, DetailView, CreateView,
	UpdateView, DeleteView
	)
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy


# Create your views here.
class BlogView(ListView):
	model = Post
	template_name = 'blog/blog.html'
	ordering = ['-blog_date']
	success_message = 'List successfully saved!!!!'


class BlogDetail(DetailView):
	model = Post
	template_name = 'blog/blog_detail.html'


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

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import PostForm, EditForm

# Create your views here.
# def blog(request):
# 	return render(request, 'blog/blog.html', {})

class BlogView(ListView):
	model = Post
	template_name = 'blog/blog.html'


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
	# fields = ['title', 'title_tag', 'body']

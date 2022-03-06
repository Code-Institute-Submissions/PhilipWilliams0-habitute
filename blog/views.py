from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

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
	template_name = 'blog/add_blog.html'
	fields = '__all__'
	#fields = ('title', 'body')

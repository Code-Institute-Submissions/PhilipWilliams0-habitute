from django.shortcuts import render
from django.views.generic import (
	ListView, DetailView, CreateView,
	UpdateView, DeleteView
	)
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy


# Create your views here.
class BlogView(ListView):
	model = Post
	template_name = 'blog/blog.html'
	ordering = ['-blog_date']
	
	def get_context_data(self, *args, **kwargs):
		cate_menu = Category.objects.all()
		context = super(BlogView, self).get_context_data(*args, **kwargs)
		context["cate_menu"] = cate_menu
		return context

class BlogDetail(DetailView):
	model = Post
	template_name = 'blog/blog_detail.html'


class AddBlogView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'blog/add_blog.html'


class AddCategoryView(CreateView):
	model = Category
	fields = '__all__'
	template_name = 'blog/add_category.html'


def CategoryListView(request):
	cate_menu_list = Category.objects.all()
	return render(request, 'blog/category_list.html', {'cate_menu_list':cate_menu_list})


def CategoryView(request, cate):
	category_blogs = Post.objects.filter(category=cate.replace('-', ' '))
	return render(request, 'blog/categories.html', {'cate':cate.title().replace('-', ' '), 'category_blogs':category_blogs})


class UpdateBlogView(UpdateView):
	model = Post
	form_class = EditForm
	template_name = 'blog/edit_blog.html'


class DeleteBlogView(DeleteView):
	model = Post
	template_name = 'blog/delete_blog.html'
	success_url = reverse_lazy('blog')

from django.urls import path
from .views import BlogView, ArticleDetail, AddBlogView, UpdateBlogView, DeleteBlogView

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('article/<int:pk>/', ArticleDetail.as_view(), name='article_detail'),
    path('add_blog/', AddBlogView.as_view(), name='add_blog'),
    path('edit_blog/<int:pk>/', UpdateBlogView.as_view(), name='edit_blog'),
    path('article/<int:pk>/delete', DeleteBlogView.as_view(), name='delete_blog'),
]

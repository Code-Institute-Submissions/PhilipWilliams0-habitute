from django.urls import path
from .views import BlogView, ArticleDetail, AddBlogView

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('article/<int:pk>/', ArticleDetail.as_view(), name='article_detail'),
    path('add_blog/', AddBlogView.as_view(), name='add_blog'),
]

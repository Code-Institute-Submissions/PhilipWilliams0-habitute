from django.urls import path
# from . import views
from .views import BlogView, BlogDetailView

urlpatterns = [
    # path("", views.blog, name="blog"),
    path('', BlogView.as_view(), name="blog"),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name="blog_detail"),
]

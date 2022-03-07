from django.urls import path
from . import views


urlpatterns = [
    path("", views.news_idx, name="news_idx")
    ]

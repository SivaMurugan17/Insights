from django.urls import path
from .views import Home,Posts,SinglePost
urlpatterns = [
    path("",Home.as_view(),name='home'),
    path('posts',Posts.as_view(),name='all-posts'),
    path('posts/<slug:slug>',SinglePost.as_view(),name='single-post')
]

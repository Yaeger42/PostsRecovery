"""Posts URLs"""

# Django imports
from django.urls import path

# Views
from posts import views

urlpatterns = [
    path(
        route = 'posts/feed/',
        view = views.PostsFeedView.as_view(),
        name = 'feed'
    ),

    path(
        route='posts/new/',
        view=views.CreatePostView.as_view(),
        name='create'
    ),
]
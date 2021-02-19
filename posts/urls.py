"""Posts URLs"""

# Django imports
from django.urls import path

# Views
from posts import views

urlpatterns = [
    path(
        route = '',
        view = views.PostsFeedView.as_view(),
        name = 'feed'
    ),

    path(
        route = 'posts/new/',
        view = views.CreatePostView.as_view(),
        name = 'create'
    ),

    path(
        route = 'posts/<pk>/delete',
        view = views.PostDeleteView.as_view(),
        name = 'delete'
    ),

    path(
        route = 'posts/<pk>',
        view = views.PostDetailView.as_view(),
        name = 'detail'
    ),
    
    path(
        route = 'posts/edit/<pk>',
        view = views.PostEditView.as_view(),
        name = 'edit'
    )
]
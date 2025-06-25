from django.urls import path
from .views import (
    LoginView,
    register_user,
    PostList,
    PostDetail,
    CreatePost,
    update_post,
    delete_post,
)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', register_user, name='register'),
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('posts/create/', CreatePost.as_view(), name='create-post'),
    path('posts/<int:pk>/update/', update_post, name='update-post'),
    path('posts/<int:pk>/delete/', delete_post, name='delete-post'),
]

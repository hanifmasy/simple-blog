from django.urls import path
from . import views

urlpatterns = [
    # User authentication
    path('api/auth/register/', views.UserRegisterView.as_view(), name='register'),
    path('api/auth/login/', views.UserLoginView.as_view(), name='login'),
    path('api/auth/logout/', views.UserLogoutView.as_view(), name='logout'),

    # Blog post CRUD endpoints
    path('api/posts/', views.BlogPostListView.as_view(), name='post-list'),
    path('api/posts/<int:pk>/', views.BlogPostDetailView.as_view(), name='post-detail'),

    # Comment CRUD endpoints
    path('api/comments/', views.CommentListView.as_view(), name='comment-list'),
    path('api/comments/<int:pk>/', views.CommentDetailView.as_view(), name='comment-detail'),

    # Like/Dislike endpoints
    path('api/posts/<int:pk>/like/', views.LikePostView.as_view(), name='like-post'),
    path('api/posts/<int:pk>/dislike/', views.DislikePostView.as_view(), name='dislike-post'),
    path('api/comments/<int:pk>/like/', views.LikeCommentView.as_view(), name='like-comment'),
    path('api/comments/<int:pk>/dislike/', views.DislikeCommentView.as_view(), name='dislike-comment'),
]

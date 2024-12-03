from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserList, UserDetail, PostList, PostDetail, CommentList, CommentDetail, CategoryList, CategoryDetail, api_root

urlpatterns = [
    path('', api_root),
    path('users/', UserList.as_view(), name="user-list"),
    path('users/<int:pk>/', UserDetail.as_view(), name="user-detail"),
    path('posts/', PostList.as_view(), name="post-list"),
    path('posts/<int:pk>/', PostDetail.as_view(), name="post-detail"),
    path('comments/', CommentList.as_view(), name="comment-list"),
    path('comments/<int:pk>/', CommentDetail.as_view(), name="comment-detail"),
    path('categories/', CategoryList.as_view(), name="category-list"),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name="category-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
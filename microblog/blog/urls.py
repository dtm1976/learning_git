from django.urls import path

from .views import index, posts_list, PostCreate, PostDetail, PostUpdate, PostDelete, PostListView


urlpatterns = [
    path('', index, name='home_url'),
    # path('posts/', posts_list, name='posts_list_url'),
    path('posts/', PostListView.as_view(), name='posts_list_url'),
    # path('post/create/', post_create, name='post_create_url'),
    path('post/create/', PostCreate.as_view(), name='post_create_url'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
    path('post/<str:slug>/update/', PostUpdate.as_view(), name='post_update_url'),
    path('post/<str:slug>/delete/', PostDelete.as_view(), name='post_delete_url'),
    # path('post/<str:slug>/', post_detail, name='post_detail_url')
    # path('<str:name>', index),
    # path('post/'),
    # path('post/create/')
]
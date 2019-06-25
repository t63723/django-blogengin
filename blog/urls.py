from django.urls import path

from .views import *

urlpatterns = [
    path('', post_list, name='posts_list_url'),
    path('post/create', PostCreate.as_view(), name='post_create_url'),
    path('post/<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('post/<slug:slug>/update/', PostUpdate.as_view(), name='post_update_url'),
    path('post/<slug:slug>/delete/', PostDelete.as_view(), name='post_delete_url'),
    path('tags/', tag_list, name='tags_list'),
    path('tags/create', TagCreate.as_view(), name='tag_create_url'),
    path('tags/<slug:slug>/', TagDetail.as_view(), name='tag_detail_url'),
    path('tags/<slug:slug>/update/', TagUpdate.as_view(), name='tag_update_url'),
    path('tags/<slug:slug>/delete/', TagDelete.as_view(), name='tag_delete_url'),
]

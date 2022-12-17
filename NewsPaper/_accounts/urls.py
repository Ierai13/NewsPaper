from django.urls import path
from .views import PostList, PostDetail, PostCreate, PostCreatePost, PostUpdate, PostSearch, PostDelete

urlpatterns = [
    path('',PostList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('create_news/', PostCreate.as_view(), name='news_create'),
    path('create_post/', PostCreatePost.as_view(), name='post_create'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('search/', PostSearch.as_view(), name='post_search'),
    path('search/<int:pk>', PostDetail.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
]

from django.urls import path
from .views import NewsList, NewsDetail, SearchNewsList, PostCreate, PostUpdate, PostDelete

urlpatterns = [
    path('news/', NewsList.as_view(), name='news_list'),
    path('news/<int:pk>', NewsDetail.as_view(), name='news_detail'),
    path('news/search/', SearchNewsList.as_view()),
    path('news/create/', PostCreate.as_view(), name='news_create'),
    path('news/<int:pk>/edit', PostUpdate.as_view(), name='news_edit'),
    path('news/<int:pk>/delete', PostDelete.as_view(), name='news_delete'),
    path('article/create/', PostCreate.as_view(), name='article_create'),
    path('article/<int:pk>/edit', PostUpdate.as_view(), name='article_edit'),
    path('article/<int:pk>/delete', PostDelete.as_view(), name='article_delete'),
]

from django.urls import path
from news.views import PostList, PostDetail, PostSearch, NewsCreate, NewsUpdate, NewsDelete, ArticlesCreate, \
   ArticlesUpdate, ArticlesDelete


urlpatterns = [

   path('', PostList.as_view(), name='post_list'),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('news/search', PostSearch.as_view(), name='post_search'),
   path('news/create/', NewsCreate.as_view(), name='news_create'),
   path('news/<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),
   path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_Delete'),
   path('articles/create/', ArticlesCreate.as_view(), name='news_create'),
   path('articles/<int:pk>/update/', ArticlesUpdate.as_view(), name='news_update'),
   path('articles/<int:pk>/delete/', ArticlesDelete.as_view(), name='news_Delete'),
]

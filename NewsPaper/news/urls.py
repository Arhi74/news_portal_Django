from django.urls import path, include
from news.views import PostList, PostDetail, PostSearch, NewsCreate, NewsUpdate, NewsDelete, ArticlesCreate, \
    ArticlesUpdate, ArticlesDelete, BaseRegisterView
from .views import upgrade_me

urlpatterns = [

    path('', PostList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('news/search', PostSearch.as_view(), name='post_search'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('news/<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('articles/create/', ArticlesCreate.as_view(), name='articles_create'),
    path('articles/<int:pk>/update/', ArticlesUpdate.as_view(), name='articles_update'),
    path('articles/<int:pk>/delete/', ArticlesDelete.as_view(), name='articles_delete'),
    path('accounts/', include('allauth.urls')),
    path('signup/', BaseRegisterView.as_view(template_name='signup.html'), name='signup'),
    path('upgrade/', upgrade_me, name='upgrade'),

]

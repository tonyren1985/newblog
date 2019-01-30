from django.conf.urls import url
from . import views
from django.conf import settings

app_name = 'article'

urlpatterns = [
    url(r'^article-column/$', views.article_column, name='article_column'),
    url(r'^rename-column/$', views.rename_article_column, name='rename_article_column'),
    url(r'^del-column/$', views.del_article_column, name='del_article_column'),
]
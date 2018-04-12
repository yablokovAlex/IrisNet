from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^news/get/(?P<news_id>\d+)/$', views.new),
    url(r'^news/addlike/(?P<news_id>\d+)/$', views.addlike),
    url(r'^news/addcomment/(?P<news_id>\d+)/$', views.addcomment),
    url(r'^', views.news),
]
